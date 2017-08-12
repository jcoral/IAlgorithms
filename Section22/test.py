# -*- coding: utf-8 -*-

from Graph import Graph
from Vertice import Vertice
from Edge import Edge

# d = {"a": {"aa": 11}, "b": {"bb": 22}}
#
# l = []
# for d1 in d.values():
#     l += d1.values()
#
# print l

import random
vertices = [Vertice(v) for v in range(7)]
nodes = [vertices[i] for i in [random.randint(0, 6) for _ in range(14)]]

_edges = [Edge(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

edges = []
for i in range(len(_edges) - 1):
    same = False
    for j in range(i + 1, len(_edges)):
        isSameSrc = _edges[i].srcVertice.id == _edges[j].srcVertice.id
        isSameDst = _edges[i].dstVertice.id == _edges[j].dstVertice.id
        if isSameDst and isSameSrc:
            same = True

    if not same:
        edges.append(_edges[i])
#
# for e in edges:
#     print e

# print len(edges)

# graph = Graph(edges)
graph = Graph.loadGraph("deepgraph.json")
# print graph.__graphDic__

def fn(srcv = None, dstv = None):
    print srcv, "  ", dstv
# print vertices[0]

def bfs(g):
    print "-" * 20 + " BFS " + "-" * 20
    g.BFS(g.__graphDic__.values()[0].values()[0].srcVertice, fn)
    print "-" * 45 + "\n"
def dfs(g, src, dst):
    print "-" * 20 + " DFS " + "-" * 20
    g.DFSA(g.__graphDic__[src][dst].srcVertice, fn, choiceChildFN=lambda s, d: s.id != "u" or d.id == "v")
    print "-" * 45 + "\n"

bfs(graph)
dfs(graph, "u", "v")


# print "-" * 14 + " Topological sort " + "-" * 14
# A = graph.topologicalSort()
# for a in A:
#     print a.value,
# print
# print "-" * 46 + "\n"
#
# graph.storeGraph("topograph.json")
#
# print graph.__graphDic__

# g = graph.transpositionGraph()
# print "Transposition"
# dfs(g, "b", "a")

# print g.__graphDic__

#
# print ""


