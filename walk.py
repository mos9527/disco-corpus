from typing import List
from dataclasses import dataclass, field
import sys


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
class graph:
    nodes: dict[int, gvNode] = field(default_factory=dict)
    edges: dict[int, List[int]] = field(default_factory=dict)

    @staticmethod
    def from_lines(lines: List[str]) -> "graph":
        g = graph()
        lines_iter = iter(lines)
        for line in lines_iter:
            """
            # WHIRLING F1 /  MERC TRIBUNAL WARNING
            # WARNING THE BOYS ABOUT MERC TRIBUNAL
            # ==================================================
            digraph G {
                      0 [label="START"];
                      1 [label="input"];
                      2 [label="You: \"I mean, 'Okay, you got one more gun on your side.' Once I find mine. I lost it.\""];
                      3 [label="Kim Kitsuragi: IsKimHere()"];
                      ...
                      0 -> 0
                      1 -> 11
                      2 -> 45
                      3 -> 3
            """
            if line.startswith("#"):
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
            pass
        return g


try:
    g = graph.from_lines(open(sys.argv[-1], encoding="utf-8").readlines())
except Exception as e:
    print(e)
    print("Usage: python walk.py <file>.gv")
    sys.exit(1)

import inquirer

u = 1
while True:
    print(g.nodes[u].label)
    choices = [f"{v}: {g.nodes[v].label}" for v in g.edges.get(u, [])]
    if not choices:
        break
    questions = [inquirer.List("next", message="Choose", choices=choices)]
    u = int(inquirer.prompt(questions)["next"].split(":")[0])
