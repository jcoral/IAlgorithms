# -*- coding: utf-8 -*-

class Edge:

    def __init__(self, srcVertice, dstVertcie):
        self.srcVertice = srcVertice
        self.dstVertice = dstVertcie
        self.weight  = 1


    def __str__(self):
        return "SRC: " + str(self.srcVertice.id) + \
               " DST: " + str(self.dstVertice.id) + \
               " Weight: " + str(self.weight)













