# -*- coding: utf-8 -*-
from Section12.Node import Node
from abc import abstractmethod

class Tree:

    def __init__(self):
        self.header = None

    @property
    def isEmpty(self):
        return self.header is None

    @abstractmethod
    def addChild(self, v): pass

    @abstractmethod
    def removeNode(self, node): pass

    def preorderWalk(self, startNode = None, fn = None):
        """
        前序遍历
        :return:
        """
        pass

    def inorderWalk(self, startNode = None, fn = None):
        """
        中序遍历
        :return:
        """
        pass

    def postorderWalk(self, startNode = None, fn = None):
        """
        后序遍历
        :return:
        """
        pass

    def find(self, v):
        pass











