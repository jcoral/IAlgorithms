# -*- coding: utf-8 -*-

class Vertice:

    def __init__(self, v, id = None):
        """
        :param v:  值
        :param id: 顶点ID
        :param _mark: 顶点标记，0：白色, 1：灰色, 2： 黑色
        :param _ft: 完成时间
        :param __minWeight__: 用于最短路径中保存源点到当前结点的最小权重
        :param __minFrontVertice: 用于保存最短路径中最小权重的前驱
        """
        self.value = v
        self._mark = 0
        self.deep  = 0
        self._ft   = 0
        self.__minWeight__ = None
        self.__minFrontVertice__ = None

        if id is None:
            self.id = str(v)
        else:
            self.id = str(id)

    @property
    def __mark__(self):
        return self._mark

    @__mark__.setter
    def __mark__(self, m):
        if m > 2: self._mark = 2
        else: self._mark = m


    def __resetVerticeStatus__(self):
        self._mark = 0
        self.deep  = 0
        self.__mark__ = 0

    def __str__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        return "Value: " + str(self.value) + \
               " ID: " + str(self.id) + \
               " minWeight: " + str(self.__minWeight__)










