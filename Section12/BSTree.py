# -*- coding: utf-8 -*-


"""
二叉搜索树
"""
from Section12.BTree import BTree
from Section12.Node import Node


class BSTree(BTree):

    def __init__(self):
        BTree.__init__(self)

    def addChild(self, v):
        """
        添加一个元素
        :param v: 值
        """
        if self.isEmpty:
            self.header = Node(v)
            return

        curNode = self.header
        while True:
            if v < curNode.value:
                # 左结点
                if curNode.left is None:
                    curNode.left = Node(v)
                    break
                else:
                    curNode = curNode.left
            else:
                # 右结点
                if curNode.right is None:
                    curNode.right = Node(v)
                    break
                else:
                    curNode = curNode.right

    def removeNode(self, node):
        # 找到父节点
        parent = self.findParent(node)
        # TODO

    def find(self, v):
        """
        查找
        :param v: 需要查找的值
        :return:  bool
        """
        if self.isEmpty: return False
        curNode = self.header
        while curNode is not None:
            value = curNode.value
            if v == value: return True
            elif v < value:
                # 左结点
                if curNode.left is None:
                    return False
                else:
                    curNode = curNode.left
            else:
                # 右结点
                if curNode.right is None:
                    return False
                else:
                    curNode = curNode.right
        return False
















