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
        """
        删除节点

        # 判断节点是不是父节点
        # 如果是父节点，则改变树的头结点指向头节点的右孩子
        # 如果不是则找到node的父节点，并将父节点的孩子指向node的右孩子
        # 最后将node的左孩子连接到node右孩子的最小节点上

        :param node: 要删除的节点
        """

        if node == self.header:
            rightNode = node.right
            self.header = node.right
        else:
            parent, pos = self.findParent(node, usePosition=True)

            rightNode = node.right
            if pos == 0:
                parent.left = rightNode
            else:
                parent.right = rightNode

        if rightNode is not None:
            minNode = rightNode.findMinLeafNode()
            minNode.left = node.left

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
















