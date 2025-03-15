import os
from concurrent.futures import ThreadPoolExecutor

ROOT = "graphviz"
OUTPUT = "svg"
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
                executor.submit(os.system, cmd)
