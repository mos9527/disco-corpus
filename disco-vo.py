import os, argparse, json
import UnityPy
from UnityPy.helpers.TypeTreeGenerator import TypeTreeGenerator
from UnityPy.enums import ClassIDType
from UnityPy.classes import MonoBehaviour

MAX_DIALOGUE = 10000

from typing import Type, TypeVar

T = TypeVar("T")


def get_class_id(cls: Type[T]) -> T:
    return None


a = get_class_id(int)


def __main__():
    parser = argparse.ArgumentParser(description="Process Disco Elysium dialogue files")
    parser.add_argument(
        "--root",
        default=r"C:\Program Files (x86)\Steam\steamapps\common\Disco Elysium",
        help="Root directory of Disco Elysium installation",
    )
    parser.add_argument(
        "--articy-map",
        default="articy_mapping.json",
        help="*INPUT* Articy ID:ConvoID.DialogueID mapping json",
    )
    parser.add_argument("output", help="Output ConvoID.DialogueID:VO Info json")
    args = parser.parse_args()
    print("Parsing Typetree info")
    from uttcg import UTTCGen_AsInstance
    from uttcg.VOTool import VoiceOverClipsLibrary

    print("Loading data")
    env = UnityPy.load(os.path.join(args.root, "disco_Data", "sharedassets1.assets"))

    mono = [
        obj.read(check_read=False)
        for obj in env.objects
        if obj.class_id == ClassIDType.MonoBehaviour
    ]
    vo_lib = next(filter(lambda x: x.m_Name == "VoiceOverClipsLibrary", mono))
    vo_lib = UTTCGen_AsInstance(VoiceOverClipsLibrary, vo_lib)

    mapping = json.load(open(args.articy_map, "r", encoding="utf-8"))
    vo = [
        (mapping.get(clip.ArticyID, "UNUSED"), clip) for clip in vo_lib.clipInformations
    ]
    vo = sorted(vo, key=lambda k: k[0])
    dump = {
        k: {
            "ab": info.AssetBundle,
            "name": info.AssetName,
            "path": info.PathToClipInProject,
        }
        for k, info in vo
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(dump, f, indent=4, ensure_ascii=False)
    pass


if __name__ == "__main__":
    __main__()
