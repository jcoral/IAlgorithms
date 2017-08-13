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
graph = Graph.loadGraph("g23_1.json")
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
    g.DFS(g.__graphDic__[src][dst].srcVertice, fn)
    print "-" * 45 + "\n"
# 搜索
# bfs(graph)
# dfs(graph, "a", "b")

# 拓扑排序
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

# 强连通图
# g = graph.transpositionGraph()
# print "Transposition"
# dfs(g, "e", "b")
# print isinstance(g, Graph)
# dfs(g, "e", "a")

# print g.__graphDic__

# 最短路径
# f = graph.__graphDic__["s"]["t"].srcVertice
# spg = graph.BellmanFord(f)
# spg.BFS(v=f,fn=fn)

# d = graph.Dijkstra(f)
# d.BFS(v=f, fn=fn)

# 最小生成树
mst = graph.Prim()
print mst.__graphDic__
dfs(mst, "a", "b")
























