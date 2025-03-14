# The Disco Elysium Corpus Project
Corpus in GraphViz format for the CRPG Disco Elysium.

This project is NOT affiliated with ZA/UM, Robert Kurvitz, or any other party involved in the creation of Disco Elysium.

# Structure
GraphViz files are stored in `graphviz` and are seperated in folders A-Z which represent the first letter of the conversation name. Each file contains a list of nodes and edges in GraphViz format.

You can view the files using any text editor or a GraphViz viewer. You can do this online using [GraphVizOnline](https://dreampuf.github.io/GraphvizOnline/).

Embedding a URL is also possible.

https://dreampuf.github.io/GraphvizOnline/?url=https://raw.githubusercontent.com/mos9527/disco-corpus/refs/heads/main/graphviz/disco-corpus-en/W/WHIRLING%20_%20BATHROOM%20MIRROR_0x010000040000032B.gv

There's also a SVG version of the graph available [in the `svg` folder.](https://github.com/mos9527/disco-corpus/tree/main/svg	)

# Example
```
# WHIRLING F1 / KIM FIRST VISIT barks
# Kim doesn't like pinball.
# ==================================================
digraph G {
	  0 [label="START"];
	  1 [label="input"];
	  2 [label="Kim Kitsuragi: \"Goddamned pinball.\""];
	  0 -> 1
	  1 -> 2
}
```