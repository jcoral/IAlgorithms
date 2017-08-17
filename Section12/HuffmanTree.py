# -*- coding: utf-8 -*-

from BTree import BTree
from Node import Node

class HuffmanTree(BTree):

    def __init__(self, nodes):
        BTree.__init__(self)
        self.header = self.generateHuffmanTree(nodes)

    def generateHuffmanTree(self, nodes):
        while True:
            f = nodes.pop(0)
            s = nodes.pop(0)

            p = Node(f.value + s.value)
            p.left = f
            p.right = s
            f.parent = p
            s.parent = p

            rindexs = range(len(nodes))
            rindexs.reverse()
            for i in rindexs:
                if nodes[i].value < p.value:
                    nodes.insert(i + 1, p)
                    break

            if len(nodes) == 0:
                return p


















