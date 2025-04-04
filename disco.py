import os, argparse, json
import UnityPy
from UnityPy.enums import ClassIDType
from UnityPy.classes import MonoBehaviour
from tqdm import tqdm
from collections import defaultdict

MAX_DIALOGUE = 10000


def escape_quotes(s: str):
    return s.replace('"', '\\"').replace("\n", "")


def escape_filename(s: str):
    ng = r'<>:"/\|?*'
    for c in ng:
        s = s.replace(c, "")
    return s


def __main__():
    parser = argparse.ArgumentParser(description="Process Disco Elysium dialogue files")
    parser.add_argument(
        "--root",
        default=r"C:\Program Files (x86)\Steam\steamapps\common\Disco Elysium",
        help="Root directory of Disco Elysium installation",
    )
    parser.add_argument(
        "--lockit-path",
        default=r"disco_Data\StreamingAssets\AssetBundles\Windows\lockits",
        help="Lockit (translation) bundle path",
    )
    parser.add_argument(
        "--dialog-path",
        default=r"disco_Data\StreamingAssets\aa\StandaloneWindows64\dialoguebundle_assets_all_3472cb598f88f38eef12cdb3aa5fdc80.bundle",
        help="dialoguebundle_assets_all bundle path",
    )
    parser.add_argument(
        "--lockit",
        default="",
        help="Lockit (translation) to use to generate translated files",
    )
    parser.add_argument(
        "--articy-map",
        default="articy_mapping.json",
        help="Where to store Articy ID:ConvoID.DialogueID mapping json",
    )
    parser.add_argument("output", help="Output directory")
    args = parser.parse_args()
    env = UnityPy.Environment()

    print("Loading environment")
    env.load_folder(os.path.join(args.root, args.lockit_path))
    env.load_file(os.path.join(args.root, args.dialog_path))

    print("Loading assets")
    mono = [obj for obj in env.objects if obj.class_id == ClassIDType.MonoBehaviour]
    dialog = dict()
    for obj in tqdm(mono):
        obj = obj.read()
        obj: MonoBehaviour
        if obj.m_Name.startswith("DialoguesLockit") or obj.m_Name.startswith("Disco"):
            dialog[obj.m_Name] = obj
        pass
    disco = dialog["Disco Elysium"]

    from_fields = lambda obj: {field.title: field.value for field in obj}

    actors = {actor.id: from_fields(actor.fields) for actor in disco.actors}

    lang_def = defaultdict(dict)
    # TODO: Argparse?
    if args.lockit:
        lockit = dialog.get(args.lockit, None)
        assert lockit, "Invalid Lockit. Pick from %s" % ",".join(dialog.keys())
        for data in lockit.mSource.mTerms:
            term, text = data.Term, data.Languages
            term = term.split("/")
            if len(term) == 1:
                cat, aid = "Unknown", term[0]
            else:
                cat, aid = term
            lang_def[aid][cat] = text

    DEST = args.output
    os.makedirs(DEST, exist_ok=True)

    articy_mapping = dict()

    def process_one(convo_id):
        convo = disco.conversations[convo_id]
        convo_fields = from_fields(convo.fields)
        cid = convo_fields.get("Articy Id", None)
        ctitle = convo_fields.get("Title", None)
        cdesc = convo_fields.get("Description", None)
        if cid and ctitle and cdesc:
            fdir = ctitle[0].upper()
            if not fdir.isalpha():
                fdir = "_"
            os.makedirs(os.path.join(DEST, fdir), exist_ok=True)
            fpath = os.path.join(DEST, fdir, f"{escape_filename(ctitle)}_{convo_id}.gv")
            f = open(fpath, "w", encoding="utf-8")
            writeline = lambda *a, **k: print(*a, **k, file=f)

            writeline("#", ctitle)
            writeline("#", "\n#".join(cdesc.split("\n")))
            writeline("#", "=" * 50)
            graph = defaultdict(set)
            entry_is_fork = (
                lambda entry: from_fields(entry.fields).get("DialogueEntryType", None)
                == "Fork"
            )
            jumpout = set()
            for entry in convo.dialogueEntries:
                for outlink in entry.outgoingLinks:
                    if convo_id + 1 != outlink.destinationConversationID:
                        dest = (
                            MAX_DIALOGUE * outlink.destinationConversationID
                            + outlink.destinationDialogueID
                        )
                        jumpout.add(dest)
                        graph[entry.id].add(dest)
                    else:
                        graph[entry.id].add(outlink.destinationDialogueID)
            writeline("digraph G {")
            for entry in convo.dialogueEntries:
                u = entry.id
                entry_fields = from_fields(entry.fields)
                aid = entry_fields.get("Articy Id", None)
                lang = lang_def.get(aid, None)

                def get_field(name):
                    fallback = entry_fields.get(name, None)
                    if lang:
                        ret = lang.get(name, fallback)
                        if ret:
                            return ret[0]
                    return fallback

                if aid:
                    articy_mapping[aid] = f"{convo.id}.{u}"
                if not entry_is_fork(entry):
                    text = get_field("Dialogue Text")
                    for alt in range(1, 10):
                        text_alt = get_field(f"Alternate{alt}")
                        if text_alt:
                            text += "\\n" + text_alt
                        else:
                            break
                    text = text or get_field("Title")

                    actor = int(entry_fields.get("Actor", 0))
                    actor = actors.get(actor, {}).get("Name", None)
                    if actor:
                        text = f"{actor}: {text}"
                    text = escape_quotes(text)
                    if text:
                        writeline(f'\t  {u} [label="{text}"];')
                else:
                    title = entry_fields.get("Title", None)
                    title = escape_quotes(title or "")
                    writeline(f'\t  {u} [label="{title}", shape=diamond];')
            for u in jumpout:
                dest = u // MAX_DIALOGUE
                convo = disco.conversations[dest - 1]
                convo_fields = from_fields(convo.fields)
                writeline(
                    f'\t  {u} [label="JUMP OUT to {convo_fields.get('Title',dest)}", shape=diamond];'
                )
            for u, edges in graph.items():
                for v in edges:
                    writeline(f"\t  {u} -> {v}")
            writeline("}")
            writeline()

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor() as executor:
        for convo_id, convo in tqdm(enumerate(disco.conversations)):
            # executor.submit(process_one, convo_id)
            process_one(convo_id)

    with open(args.articy_map, "w", encoding="utf-8") as f:
        json.dump(articy_mapping, f)


if __name__ == "__main__":
    __main__()
