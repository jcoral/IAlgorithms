# -*- coding: utf-8 -*-

class Edge:

    def __init__(self, srcVertice, dstVertcie, weight = 1):
        self.srcVertice = srcVertice
        self.dstVertice = dstVertcie
        self.weight  = weight
        self.__mark__ = 0

    def __cmp__(self, other):
        return self.weight - other.weight

    def __str__(self):
        return "SRC: " + str(self.srcVertice.id) + \
               " DST: " + str(self.dstVertice.id) + \
               " Weight: " + str(self.weight) + \
               " Mark: " + str(self.__mark__)













