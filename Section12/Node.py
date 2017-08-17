# -*- coding: utf-8 -*-
import math

class Node():

    def __init__(self, v = None):
        self.left  = None
        self.right = None
        self.value = v

    def isParent(self, node, usePosition=False):
        """
        判断node是不是当前结点的孩子
        :param node: 孩子
        :param usePosition: 是否返回孩子的位置， 0：左孩子， 1：右孩子
        :return: usePostion true: (bool, position) false: bool
        """
        _ip = self.left == node
        if usePosition:
            position = 0
        if self.right == node:
            position = 1
            _ip = True

        if usePosition:
            return (_ip, position)
        else:
            return _ip

    def findMinLeafNode(self):
        leaf = self
        while leaf.left is not None:
            leaf = leaf.left
        return leaf

    def findMaxLeafNode(self):
        leaf = self
        while leaf.right is not None:
            leaf = leaf.right
        return leaf

    def __cmp__(self, other):
        dif = self.value - other.value
        if dif < 0:
            return int(math.floor(dif))
        else:
            return int(math.ceil(dif))

    def __str__(self):
        return "Value: " + str(self.value)






























