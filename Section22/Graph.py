# -*- coding: utf-8 -*-
from Vertice import Vertice
from Edge import Edge
from copy import deepcopy

"""
图

存放规则
{
    srcID: {dstID1: edge1, ...}
    ...
}

"""

class Graph:

    verticeConnctionChar = "->"
    weightAndEdgeConnectionChar = ":"

    def __init__(self, edges = None):
        self.__graphDic__ = {}
        if edges is not None:
            for edge in edges:
                self.addEdge(edge)

    @property
    def vertices(self):
        """ 获取所有的顶点 """
        vs = set()
        for de in self.__graphDic__.values():
            for edge in de.values():
                vs.add(edge.srcVertice)
                vs.add(edge.dstVertice)

        return vs

    @property
    def edges(self):
        """ 获取所有的边 """
        es = []
        for de in self.__graphDic__.values():
            es += de.values()

        return es

    @property
    def __firstEdge__(self):
        return self.__graphDic__.values()[0].values()[0]

    def getEdge(self, srcv, dstv):
        """
        根据起点到终点获取边的权重
        :param srcv: 起点
        :param dstv: 终点
        :return: srcv到dstv的边
        """
        if isinstance(srcv, Vertice) and isinstance(dstv, Vertice):
            srcId = srcv.id
            dstId = dstv.id
        else:
            srcId = srcv
            dstId = dstv
        if self.__graphDic__.__contains__(srcId) and self.__graphDic__[srcId].__contains__(dstId):
            return self.__graphDic__[srcId][dstId]
        return None

    def getWeight(self, srcv, dstv):
        """
        根据起点到终点获取边的权重
        :param srcv: 起点
        :param dstv: 终点
        :return: 权重
        """
        return self.getEdge(srcv, dstv)

    def addEdge(self, edge):
        """
        添加一条边
        :param edge: 边
        :return:
        """
        srcID = edge.srcVertice.id
        dstID = edge.dstVertice.id
        if not self.__graphDic__.__contains__(srcID):
            self.__graphDic__[srcID] = {}

        self.__graphDic__[srcID][dstID] = edge

    def removeEdge(self, edge):
        del self.__graphDic__[edge.srcVertice.id][edge.dstVertice.id]

    def removeEdge(self, srcv, dstv):
        e = self.getEdge(srcv, dstv)
        if e is not None:
            self.removeEdge(e)

    def unionGraph(self, graph):
        def unionEdge(edge):
            self.addEdge(edge)
        graph.mapEdges(fn=unionEdge)

    def sameEdgeUG(self, e1, e2):
        return e1.srcVertice == e2.dstVertice and e1.dstVertice == e2.srcVertice

    def mapVertices(self, id = None, fn = None, filterFN = None):
        """
        遍历节点
        :param id: None: 所有的节点, id: 与id节点相连所有结点
        :param fn: fn(vertice) 对每一个节点所要进行的操作
        :param filterFN: (vertice) -> Bool 过滤结点
        :return: 返回所有的节点
        """
        if id is None:
            vs = self.vertices
        else:
            vs = set()
            if not self.__graphDic__.__contains__(id): return
            for edge in self.__graphDic__[id].values():
                vs.add(edge.dstVertice)

        i = 0
        vs = list(vs)
        while i < len(vs):
            if filterFN is None or (filterFN is not None and filterFN(vs[i])):
                if fn is not None:
                    fn(vs[i])
                i += 1
            else:
                vs.pop(i)

        return vs

    def mapEdges(self, id = None, fn = None, needSorted=False, filterUGEdge=False, filterFN = None):
        """
        遍历边
        :param id: None：所有的边，id：与id节点相连的边
        :param fn: fn(edge) 对每一个边所要进行的操作
        :param needSorted: 对边是否需要排序
        :param filterUGEdge: 对无向图的边去重复
        :param filterFN: (edge) -> Bool 过滤边
        :return: 返回所有的边
        """
        if id is None: es = self.edges
        else: es = self.__graphDic__[id].values()

        if needSorted:
            es.sort()

        if filterUGEdge:
            i = 0
            while i < len(es):
                j = i + 1
                while j < len(es):
                    sameEdge = self.sameEdgeUG(es[i], es[j])
                    if sameEdge:
                        es.pop(i)
                        break
                    j += 1
                else:
                    i += 1

        i = 0
        while i < len(es):
            if filterFN is None or (filterFN is not None and filterFN(es[i])):
                if fn is not None:
                    fn(es[i])
                i += 1
            else:
                es.pop(i)

        return es

    def BFS(self, v, fn):
        """广度优先搜索

        给定一个起始节点开始遍历
        初始化一个队列vqueue，并将初始节点加进去
        开始循环，直到vqueue为空
            取队列中的第一个元素，将标记为黑色
            调用fn方法
            获取该元素指向的所有子节点
            如果子节点为白色，则添加到队列当中
            并将深度设置为父节点的深度加一
            将子节点的标记设为下一个状态
        结束循环
        重置节点的状态

        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param v: 顶点
        """

        self.__BFSTravel__(v, fn)

        # 恢复节点的初始状态
        self.__resetVerticesStatus__()

    def DFS(self, v, fn, reverse=True, choiceChildsFN=None):
        """深度优先搜索

        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param v: 顶点
        :param choiceChildsFN: (srcVertice) -> [vertices] 进行深度遍历时选择一个结点进行遍历
        :param reverse: 是否以前进式获取顶点
        """
        vstack = None
        if reverse:
            vstack = [(None, v)]
        # 从v开始搜遍历
        ft = [0]
        v.__mark__ = 1
        ft[0] = self.__DFSTravel__(v, fn, vstack, choiceChildsFN=choiceChildsFN)
        if not reverse: fn(None, v)

        # 在__graphDic__中查找未遍历过的顶点
        # 如果存在自己到自己的顶点， 则先存放到selfToSelfVertices中
        # 否则则以此顶点为起点继续进行搜索
        selfToSelfVertices = set()
        def findVerticeMarkWithZero(v):
            if v.__mark__ == 0:
                notSame = True
                if self.__graphDic__.__contains__(v.id):
                    vchilds = self.__graphDic__[v.id]
                    if vchilds.__contains__(v.id):
                        selfToSelfVertices.add(v)
                        notSame = False
                if notSame:
                    v.deep = ft[0] + 1
                    if reverse: vstack.append((None, v))
                    ft[0] = self.__DFSTravel__(v, fn, vstack, choiceChildsFN)
                    if not reverse: fn(None, v)

        self.mapVertices(fn=findVerticeMarkWithZero)

        # 遍历自己到自己的节点
        for v in selfToSelfVertices:
            if v.__mark__ == 0:
                ft[0] += 1
                v._ft = ft[0]
                if reverse: vstack.append((None, v))
                else: fn(None, v)

        if reverse:
            while len(vstack) != 0:
                fn(*vstack.pop(0))

        # 恢复所有顶点的状态
        self.__resetVerticesStatus__()

    def topologicalSort(self):
        """
        拓扑排序
        :return: 排序后的结果
        """
        try:
            v = self.__graphDic__.values()[0].values()[0].srcVertice
        except: return
        A = []
        def insertVertice(srcVertice, dstVertice):
            if srcVertice is None:
                A.insert(0, dstVertice)
            else:
                try:
                    srcIndex = A.index(srcVertice)
                    if srcVertice.id == dstVertice.id:
                        return
                except:
                    srcIndex = -1
                A.insert(srcIndex + 1, dstVertice)

        self.DFS(v, fn=insertVertice)
        return A

    def transpositionGraph(self):
        graph = Graph()
        def swapSrcWithDst(edge):
            graph.addEdge(Edge(edge.dstVertice, edge.srcVertice))

        self.mapEdges(fn=swapSrcWithDst)
        return graph

    def BellmanFord(self, s):
        """
        一般情况下用于求单源最短路径问题
        :return: 最短路径
        """
        return self.__GLP__(s, choiceIndexFN=lambda q: 0)

    def Dijkstra(self, s):
        """
        带权重的有向图单源最短路径问题(权重非负)
        :return: 最短路径
        """
        return self.__GLP__(s, choiceIndexFN=lambda vqueue: vqueue.index(min(vqueue)))

    def generateSSCGraph(self):
        Gt = self.transpositionGraph()

        def arriveAtV(srcv, dstv):
            pass
        self.DFS(self.__firstEdge__.srcVertice, fn=arriveAtV)

    def Prim(self):
        """最小生成树

        思想：
        初始化最小生成树
        初始化数组vqueue， 初始值为随机一个顶点指向的所有边
        循环获取数组的内容， 数组为空
            在数组中弹出边权重最小的边
            设置边两端的顶点为已经走过， 并且是双向的
            在最小生成树中添加该条边以及该边的反向边
            将改边的终点所指向的边添加到队列中，且边的终点没有走过
        结束循环
        重置图的状态

        :return 最小生成树
        """

        mst = Graph()
        def edgePass(edge, m1, m2 = None):
            if m2 is None:
                m2 = m1
            return edge.srcVertice.__mark__ == m1 and edge.dstVertice.__mark__ == m2

        def setEdgeMark(edge, m1, m2 = None):
            if m2 is None:
                m2 = m1
            edge.srcVertice.__mark__ = m1
            edge.dstVertice.__mark__ = m2

        def initEdge(edge):
            edge.__mark__ = 1
        vqueue = self.mapEdges(id=self.__firstEdge__.srcVertice.id, fn=initEdge)

        while len(vqueue) != 0:
            edge = vqueue.pop(vqueue.index(min(vqueue)))
            if edgePass(edge, 2):
                continue
            setEdgeMark(edge, 2)
            setEdgeMark(self.getEdge(edge.dstVertice, edge.srcVertice), 2)

            mst.addEdge(edge)
            mst.addEdge(self.getEdge(edge.dstVertice, edge.srcVertice))
            edges = self.mapEdges(id = edge.dstVertice.id)
            if edges is None: continue
            for child in edges:
                isPass = child.dstVertice.__mark__ == 0
                if isPass:
                    vqueue.append(child)
        self.__resetVerticesStatus__()
        return deepcopy(mst)

    def Kruskakl(self):
        """最小生成树

        思想：
        在所有的边中选取权重最小的边插入到子图中，选取完后从待选集合中删除掉
        在插入的时候需要判断边是不是安全边，如果不是则舍弃

        安全边：设A是某棵最小生成树的子集，选取的边Edge(u, v) 要满足A ∪ {Edge(u, v)}也是某棵最小生成树的子集
        """

        # 存放产生的子图
        treeSet = []

        def findVertice(e):
            """
            查找边的srcVertice和dstVertice属于哪一个子图
            :param e: 边
            :return: [g1, g2]
            """
            srcv = e.srcVertice
            dstv = e.dstVertice
            uvPosition = [None, None]
            for tree in treeSet:
                result = tree.mapVertices(filterFN=lambda v0: v0 == dstv or v0 == srcv)
                resultLength = len(result)
                if resultLength == 1:
                    if srcv == result[0]:
                        uvPosition[0] = tree
                    else:
                        uvPosition[1] = tree
                elif resultLength == 2:
                    uvPosition[0] = tree
                    uvPosition[1] = tree

                if uvPosition[0] is not None and uvPosition[1] is not None: return uvPosition

            return uvPosition

        def generateTree(edge):
            g = Graph()
            g.addEdge(edge)
            g.addEdge(self.getEdge(edge.dstVertice, edge.srcVertice))
            treeSet.append(g)

        def addMSTEdge(edge):
            srct, dstt = findVertice(edge)
            targetTree = None

            if srct == dstt and srct is not None: return

            # 如果变没有在任何一棵树中，则生成一棵树
            if srct is None and dstt is None:
                generateTree(edge)
                return

            # 边的终点在dstt树中
            if srct is None and dstt is not None: targetTree = dstt

            # 边的源点在srct树中
            if srct is not None and dstt is None: targetTree = srct

            # 如果边的源点和终点不在同一棵树中
            # 则合并两棵树
            if srct != dstt and srct is not None and dstt is not None:
                srct.unionGraph(dstt)
                treeSet.remove(dstt)
                targetTree = srct
                dstt = None

            if targetTree is not None:
                targetTree.addEdge(edge)
                targetTree.addEdge(self.getEdge(edge.dstVertice, edge.srcVertice))

        self.mapEdges(fn=addMSTEdge, needSorted=True, filterUGEdge=True)
        self.__resetVerticesStatus__()
        return deepcopy(treeSet[0])

    def __relax__(self, edge, vqueue):
        srcv = edge.srcVertice
        dstv = edge.dstVertice

        sdWeight = srcv.__minWeight__ + edge.weight
        if dstv.__minWeight__ is None or dstv.__minWeight__ > sdWeight:
            dstv.__minWeight__ = sdWeight
            dstv.__minFrontVertice__ = srcv

            if sdWeight > 0 and not vqueue.__contains__(dstv):
                vqueue.append(dstv)

    def __GLP__(self, s, choiceIndexFN):
        """
        生成最短路径

        初始化队列vqueue，初始值为s
        循环取队列的值作为srcv，直到队列为空
            获取srcv所有指向的边
            遍历srcv所有指向的边
                如果边终点的权值大于srcv的权值加上边的权值
                    修改终点的权值
                    将终点所有指向边的顶点添加到队列中
        结束循环

        :param s: 源点
        :param choiceIndexFN: 弹出队列的哪一个
        :return:
        """
        s.__minWeight__ = 0
        vqueue = [s]
        while len(vqueue) != 0:
            srcv = vqueue.pop(choiceIndexFN(vqueue))
            edges = self.mapEdges(id=srcv.id)
            for edge in edges:
                self.__relax__(edge, vqueue)
                if vqueue.__contains__(s):
                    vqueue.remove(s)

        shortestPath = Graph()
        def addEdge(v):
            edge = self.getEdge(v.__minFrontVertice__, v)
            shortestPath.addEdge(edge)

        self.mapVertices(fn=addEdge, filterFN=lambda v: v != s)
        return deepcopy(shortestPath)

    def __DFSTravel__(self, v, fn, vstack=None, choiceChildsFN=None):
        if choiceChildsFN is None:
            childs = self.mapVertices(id = v.id)
        else:
            childs = choiceChildsFN(v)
        if childs is None: childs = []
        deep = v.deep
        ft = deep + 1
        for child in childs:
            if child.__mark__ == 0 and child != v:
                child.__mark__ = 1
                child.deep = ft
                if vstack is not None: vstack.append((v, child))
                ft = self.__DFSTravel__(child, fn, vstack, choiceChildsFN) + 1
                child.__mark__ = 2
                if vstack is None: fn(v, child)

        v._ft = ft
        return ft

    def __BFSTravel__(self, v, fn):
        """
        遍历图
        :param v: 起始节点
        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param popIndex: 弹出数字的哪一个索引，n： 第n个， None：最后一个
        """
        dstv = v
        dstv.__mark__ = 1
        vqueue = [(None, dstv)]

        while len(vqueue) != 0:
            srcv, dstv = vqueue.pop(0)
            dstv.__mark__ = 2
            fn(srcv, dstv)
            childs = self.mapVertices(id = dstv.id)
            if childs is None: continue
            for child in childs:
                if child.__mark__ == 0:
                    vqueue.append((dstv, child))
                    child.deep = dstv.deep + 1
                child.__mark__ += 1

    def __resetVerticesStatus__(self):
        """ 恢复所有结点的状态 """
        def resetVerticeFN(v):
            v.__resetVerticeStatus__()

        self.mapVertices(fn=resetVerticeFN)

    @classmethod
    def __transfromEdgeToStr__(edge):
        return str(edge.weight) + Graph.weightAndEdgeConnectionChar + \
               str(edge.srcVertice.value) + Graph.verticeConnctionChar + \
               str(edge.dstVertice.value)

    @classmethod
    def __transfromEdge__(edgeStr):
        """
        :param edgeStr: srcv_value->dstv_value or weight:srcv_value->dstv_value
        :return: 带权重 (srcv_value, dstv_value, weight)
        """
        if edgeStr.__contains__(Graph.weightAndEdgeConnectionChar):
            weightAndEdges = edgeStr.split(Graph.weightAndEdgeConnectionChar)
            vs = weightAndEdges[1].split(Graph.verticeConnctionChar)
            vs.append(float(weightAndEdges[0]))
        else:
            vs = edgeStr.split("->")
            vs.append(1)
        return vs

    def storeGraph(self, fp):
        """
        存储图
        :param fp: 文件路径
        """
        import json
        f = open("fp", "w")
        json.dump(self.__graphDic__, f, default=Graph.__transfromEdgeToStr__)
        f.close()

    @classmethod
    def generateGraph(gDic):
        """
        根据图字典生成图
        :param gDic: 图字典
        :return: 图
        """
        graph = Graph()
        vDic = {}
        for srcId, dstDic in zip(gDic.keys(), gDic.values()):
            for dstId, srcToDstValue in zip(dstDic.keys(), dstDic.values()):
                srcValue, dstValue, weight = Graph.__transfromEdge__(srcToDstValue)
                srcVertice = vDic.get(srcId, Vertice(srcValue, id = srcId))
                vDic[srcId] = srcVertice
                dstVertice = vDic.get(dstId, Vertice(dstValue, id = dstId))
                vDic[dstId] = dstVertice

                graph.addEdge(Edge(srcVertice, dstVertice, weight=weight))

        return graph

    @classmethod
    def loadGraph(fp):
        """
        根据文件路径的内容生成图
        :param fp: 文件路径
        :return: 图
        """
        import json
        f = open(fp)
        graphDic = json.load(f, encoding="utf-8")
        f.close()
        return Graph.generateGraph(graphDic)












