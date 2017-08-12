# -*- coding: utf-8 -*-


class Node():

    def __init__(self, v = None):
        self.left  = None
        self.right = None
        self.value = v

    def isParent(self, node):
        return self.left == node and self.right == node

    def __str__(self):
        return "Value: " + str(self.value)












