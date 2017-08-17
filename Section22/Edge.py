# -*- coding: utf-8 -*-

import math

class Edge:

    def __init__(self, srcVertice, dstVertcie, weight = 1):
        self.srcVertice = srcVertice
        self.dstVertice = dstVertcie
        self.weight  = weight
        self.__mark__ = 0

    def __cmp__(self, other):
        dif = self.weight - other.weight
        if dif < 0:
            return int(math.floor(dif))
        else:
            return int(math.ceil(dif))

    def __str__(self):
        return "SRC: " + str(self.srcVertice.id) + \
               " DST: " + str(self.dstVertice.id) + \
               " Weight: " + str(self.weight) + \
               " Mark: " + str(self.__mark__)













