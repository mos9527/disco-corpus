import os, argparse, json, tqdm
import UnityPy
from UnityPy.helpers.TypeTreeGenerator import TypeTreeGenerator
from UnityPy.enums import ClassIDType
from UnityPy.classes import MonoBehaviour

MAX_DIALOGUE = 10000


def __main__():
    args = argparse.ArgumentParser(description="Process Disco Elysium dialogue files")
    args.add_argument(
        "--aa-dir",
        help="Path to game's StreamingAssets/aa/StandaloneWindows64 directory",
        default=r"C:\Program Files (x86)\Steam\steamapps\common\Disco Elysium\disco_Data\StreamingAssets\aa\StandaloneWindows64",
    )
    args.add_argument(
        "--output",
        help="Path to output JSON file",
        default="aa_mapping.json",
    )
    args = args.parse_args()
    # os.walk
    mapping = dict()
    bundles = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(args.aa_dir)
        for file in files
        if file.endswith(".bundle")
    ]
    for bundle in tqdm.tqdm(bundles):
        env = UnityPy.load(bundle)
        for obj in filter(lambda x: x.type == ClassIDType.AudioClip, env.objects):
            obj = obj.read()
            mapping[obj.m_Name] = os.path.basename(bundle)
        pass
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    __main__()
