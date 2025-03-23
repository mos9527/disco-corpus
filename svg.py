import os, logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
ROOT = "graphviz"
OUTPUT = "svg"


def execute(cmd):
    logger.debug(cmd)
    os.system(cmd)
    logger.debug(f"Done: {cmd}")


with ThreadPoolExecutor() as executor:
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".gv"):
                fpath = os.path.join(root, file)
                opath = os.path.join(OUTPUT, root[len(ROOT) + 1 :])
                os.makedirs(opath, exist_ok=True)
                opath = os.path.join(opath, f"{file}.svg")
                cmd = f'dot -Tsvg "{fpath}" -o "{opath}"'
                print(cmd)
                executor.submit(execute, cmd)
