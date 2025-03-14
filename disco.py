import os
import UnityPy
from UnityPy.enums import ClassIDType
from UnityPy.classes import MonoBehaviour
from tqdm import tqdm
from collections import defaultdict

ROOT = r"C:\Program Files (x86)\Steam\steamapps\common\Disco Elysium"
LOCKIT = r"disco_Data\StreamingAssets\AssetBundles\Windows\lockits"
DIALOG = r"disco_Data\StreamingAssets\aa\StandaloneWindows64\dialoguebundle_assets_all_3472cb598f88f38eef12cdb3aa5fdc80.bundle"
env = UnityPy.Environment()
print("loading environment")
env.load_folder(os.path.join(ROOT, LOCKIT))
env.load_file(os.path.join(ROOT, DIALOG))
print("loading assets")
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
all_graph = {convo.id: convo.dialogueEntries for convo in disco.conversations}


def escape_quotes(s: str):
    return s.replace('"', '\\"')


def escape_filename(s: str):
    ng = r'<>:"/\|?*'
    for c in ng:
        s = s.replace(c, "_")
    return s


lockit = dialog["DialoguesLockitChinese"]
lang_def = defaultdict(dict)
# TODO: Argparse?
if False:
    for data in lockit.mSource.mTerms:
        term, text = data.Term, data.Languages
        term = term.split("/")
        if len(term) == 1:
            cat, aid = "Unknown", term[0]
        else:
            cat, aid = term
        lang_def[aid][cat] = text

DEST = "disco-corpus-en"
os.makedirs(DEST, exist_ok=True)


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
        fpath = os.path.join(DEST, fdir, f"{escape_filename(ctitle)}_{cid}.gv")
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
        for entry_id, entry in enumerate(convo.dialogueEntries):
            for outlink in entry.outgoingLinks:
                if convo_id + 1 == outlink.destinationConversationID:
                    entry_fields = from_fields(entry.fields)
                    graph[entry_id].add(outlink.destinationDialogueID)
        writeline("digraph G {")
        for u, entry in enumerate(convo.dialogueEntries):
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
