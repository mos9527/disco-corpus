from typing import List
from dataclasses import dataclass, field
import os, argparse, random

MAX_DIALOGUE = 10000


class dict_missingKey(dict):
    def __missing__(self, key):
        return key


@dataclass
class gvNode:
    label: str
    shape: str = "ellipse"

    @staticmethod
    def from_line(s: str) -> "gvNode":
        assert s[0] == "[" and s[-2:] == "];"
        # [label="IsKimHere()", shape=diamond];
        return eval(f"_({s[1:-2]})", dict_missingKey({"_": gvNode}))


@dataclass
class gvGraph:
    comment: str = ""
    nodes: dict = field(default_factory=dict)
    edges: dict = field(default_factory=dict)

    @staticmethod
    def from_lines(lines: list) -> "gvGraph":
        g = gvGraph()
        lines_iter = iter(lines)
        for line in lines_iter:
            if line.startswith("#"):
                g.comment += line
                continue
            if line.startswith("digraph G {"):
                continue
            line = line.strip("\t \n")
            if line.endswith("}"):
                break
            num, op1 = line.split(" ", 1)
            if op1.split(" ")[0] == "->":
                u, v = line.split(" -> ")
                g.edges.setdefault(int(u), list()).append(int(v))
            else:
                while not op1.endswith(";"):
                    op1 += next(lines_iter).strip("\t \n")
                g.nodes[int(num)] = gvNode.from_line(op1)
        return g


expand_file = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder",
        help="Path to the folder containing the .gv files",
        default=None,
    )
    parser.add_argument("--start", help="Starting convo ID", default=-1, type=int)
    parser.add_argument(
        "--random", help="Randomly pick convo options", action="store_true"
    )
    parser.add_argument(
        "--speech-only",
        help="Only show speech options (no jumps, no forks)",
        action="store_true",
    )
    args = parser.parse_args()
    id_map = dict()
    if not args.folder:
        choices = [
            "graphviz/disco-corpus-cn",
            "graphviz/disco-corpus-en",
        ] + os.listdir()
        choices = [expand_file(x) for x in choices]
        choices = list(filter(os.path.exists, choices))
        import inquirer

        questions = [inquirer.List("folder", message="Source", choices=choices)]
        ans = inquirer.prompt(questions)
        if ans:
            args.folder = ans["folder"]
        else:
            raise SystemExit
        print("Loading .gv files...", args.folder)
    for root, _, files in os.walk(args.folder):
        for file in files:
            if file.endswith(".gv"):
                # TITLE_{id}.gv
                path = os.path.join(root, file)
                cid = int(file.split("_")[-1].split(".")[0])
                id_map[cid] = path
    if not id_map:
        print("No .gv files found in", args.folder)
        raise SystemExit

    def choose_convo():
        choices = [
            f"{cid}: {os.path.basename(id_map[cid])}" for cid in sorted(id_map.keys())
        ]
        import inquirer

        questions = [inquirer.List("convo", message="Convo", choices=choices)]
        ans = inquirer.prompt(questions)
        if ans:
            return int(ans["convo"].split(":")[0])
        else:
            raise SystemExit

    if args.start == -1:
        convo_id = choose_convo()
    else:
        convo_id = args.start
    diag_id = 1
    while True:
        graph = gvGraph.from_lines(open(id_map[convo_id], encoding="utf-8").readlines())
        print(graph.comment)

        vis = set()
        while True:
            node = graph.nodes.get(diag_id, None)
            if args.speech_only:
                if node.shape == "ellipse" and ":" in node.label:
                    speaker, text = node.label.split(":", 1)
                    text = text.strip()
                    if not speaker.lower().startswith("jump"):
                        if (
                            not "=" in text
                            and not "[" in text
                            and not "_" in text
                            and not "()" in text
                        ):
                            print("<%s>" % speaker, text.strip())
            else:
                lines = node.label.split("\n")
                print("//".join(lines))

            choices = [
                f"{v}: {graph.nodes[v].label.split('\n')[0]}"
                for v in graph.edges.get(diag_id, [])
            ]
            if not choices:
                if args.start == -1:
                    convo_id = choose_convo()
                    diag_id = 1
                    break
                else:
                    raise SystemExit
            if args.random:
                while diag_id in vis:
                    diag_id = random.choice(graph.edges[diag_id])
                vis.add(diag_id)
            else:
                import inquirer

                questions = [inquirer.List("next", message="Dialogue", choices=choices)]
                ans = inquirer.prompt(questions)
                if ans:
                    diag_id = int(ans["next"].split(":")[0])
                else:
                    if args.start == -1:
                        convo_id = choose_convo()
                        diag_id = 1
                        break
                    else:
                        raise SystemExit
            if diag_id:
                cur_convo_id = diag_id // MAX_DIALOGUE
                if cur_convo_id:
                    convo_id = cur_convo_id - 1
                    diag_id = diag_id % MAX_DIALOGUE
                    break
            else:
                raise SystemExit


if __name__ == "__main__":
    __main__()
