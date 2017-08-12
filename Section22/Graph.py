# -*- coding: utf-8 -*-
from Vertice import Vertice
from Edge import Edge

"""
图

存放规则
{
    srcID: {dstID1: edge1, ...}
    ...
}

"""

class Graph:

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

    def mapVertices(self, id = None, fn = None):
        """
        遍历节点
        :param id: None: 所有的节点, id: 与id节点相连所有结点
        :param fn: fn(vertice) 对每一个节点所要进行的操作
        :return: 返回所有的节点
        """
        if id is None:
            vs = self.vertices
        else:
            vs = set()
            if not self.__graphDic__.__contains__(id): return
            for edge in self.__graphDic__[id].values():
                vs.add(edge.srcVertice)
                vs.add(edge.dstVertice)

        if fn is not None:
            for v in vs:
                fn(v)

        return vs

    def mapEdges(self, id = None, fn = None):
        """
        遍历边
        :param id: None：所有的边，id：与id节点相连的边
        :param fn: fn(edge) 对每一个边所要进行的操作
        :return: 返回所有的边
        """
        if id is None: es = self.edges
        else: es = self.__graphDic__[id].values()

        if fn is not None:
            for e in es:
                fn(e)

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

        self.__travelGraph__(v, fn, 0)

        # 恢复节点的初始状态
        self.__resetVerticesStatus__()

    def DFS(self, v, fn, choiceChildFN=None):
        """深度优先搜索

        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param v: 顶点
        :param choiceChildFN: (srcVertice, dstVertice) -> Bool 进行深度遍历时选择一个结点进行遍历
        """
        # 从v开始搜遍历
        ft = [0]
        ft[0] = self.__BFSTravel__(v, fn, choiceChildFN=choiceChildFN)

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
                    ft[0] = self.__BFSTravel__(v, fn, ft=ft[0], choiceChildFN=choiceChildFN)

        self.mapVertices(fn=findVerticeMarkWithZero)

        # 遍历自己到自己的节点
        for v in selfToSelfVertices:
            if v.__mark__ == 0:
                ft[0] += 1
                v._ft = ft[0]
                fn(None, v)

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
            # print edge

        self.mapEdges(fn=swapSrcWithDst)
        return graph

    def generateSSCs(self):
        pass

    def __BFSTravel__(self, v, fn, ft=None, choiceChildFN = None):
        dstv = v
        if ft is not None:
            dstv.deep = ft + 1
            ft += 2
        dstv.__mark__ = 1
        vstack = [(None, dstv)]
        while True:
            srcv, dstv = vstack[len(vstack) - 1]
            childs = self.mapVertices(id = dstv.id)
            if childs is None: childs = []
            for child in childs:
                if child.__mark__ == 0:
                    if choiceChildFN is None or (choiceChildFN is not None and choiceChildFN(dstv, child)):
                        child.deep = dstv.deep + 1
                        child.__mark__ = 1
                        vstack.append((dstv, child))
                        break
            else:
                vl = len(vstack)
                finshedTime = ft
                if vl != 0 and ft is None: finshedTime = vstack[vl - 1][1].deep
                while True:
                    if vl == 0: return finshedTime
                    lastSrcVertice, lastDstVertice = vstack.pop(vl -1)

                    finshedTime += 1
                    lastDstVertice._ft = finshedTime
                    lastDstVertice.__mark__ = 2

                    fn(lastSrcVertice, lastDstVertice)
                    vl = len(vstack)

    def __travelGraph__(self, v, fn, popIndex):
        """
        遍历图
        :param v: 起始节点
        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param popIndex: 弹出数字的哪一个索引，n： 第n个， None：最后一个
        """
        v.__mark__ = 1
        vqueue = [v]

        while len(vqueue) != 0:
            if popIndex is None:
                v = vqueue.pop(len(vqueue) - 1)
            else:
                v = vqueue.pop(popIndex)
            v.__mark__ = 2
            fn(v)
            childs = self.mapVertices(id = v.id)
            if childs is None: continue
            for child in childs:
                if child.__mark__ == 0:
                    vqueue.append(child)
                    child.deep = v.deep + 1
                child.__mark__ += 1

    def __travelGrapho__(self, v, fn, popIndex):
        """
        遍历图
        :param dstv: 起始节点
        :param fn: fn(srcVertice, dstVertice) 对每一个节点所要进行的操作
        :param popIndex: 弹出数字的哪一个索引，n： 第n个， None：最后一个
        """
        dstv = v
        dstv.__mark__ = 1
        vqueue = [(None, dstv)]

        while len(vqueue) != 0:
            if popIndex is None:
                srcv, dstv = vqueue.pop(len(vqueue) - 1)
            else:
                srcv, dstv = vqueue.pop(popIndex)
            dstv.__mark__ = 2
            fn(srcv, dstv)
            childs = self.mapVertices(id = dstv.id)
            if childs is None: continue
            for child in childs:
                if child.__mark__ == 1 and popIndex is None:
                    for index in range(len(vqueue)):
                        if child == vqueue[index][1]:
                            src, dst = vqueue.pop(index)
                            dst.deep = dstv.deep + 1
                            vqueue.append((dstv, dst))
                            break
                else:
                    if child.__mark__ == 0:
                        vqueue.append((dstv, child))
                        child.deep = dstv.deep + 1
                    child.__mark__ += 1

    def __resetVerticesStatus__(self):
        """ 恢复所有结点的状态 """
        def resetVerticeFN(v):
            v.__resetVerticeStatus__()

        self.mapVertices(fn=resetVerticeFN)

    @staticmethod
    def __transfromEdgeToStr__(edge):
        return str(edge.srcVertice.value) + "->" + str(edge.dstVertice.value)

    @staticmethod
    def __transfromEdge__(edgeStr):
        return edgeStr.split("->")

    def storeGraph(self, fp):
        """
        存储图
        :param fp: 文件路径
        """
        import json
        f = open("fp", "w")
        json.dump(self.__graphDic__, f, default=Graph.__transfromEdgeToStr__)
        f.close()

    @staticmethod
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
                srcValue, dstValue = Graph.__transfromEdge__(srcToDstValue)
                srcVertice = vDic.get(srcId, Vertice(srcValue, id = srcId))
                vDic[srcId] = srcVertice
                dstVertice = vDic.get(dstId, Vertice(dstValue, id = dstId))
                vDic[dstId] = dstVertice

                graph.addEdge(Edge(srcVertice, dstVertice))

        return graph

    @staticmethod
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













