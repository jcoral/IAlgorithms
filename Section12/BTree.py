# -*- coding: utf-8 -*-
from Section12.Tree import Tree
from Node import Node

"""
二叉树
"""
class BTree(Tree):

    def __init__(self):
        Tree.__init__(self)

    @property
    def height(self):
        return self.__height__(self.header) + 1

    def __height__(self, startNode):
        left  = 0
        right = 0
        if startNode.left is not None:
            left = self.__height__(startNode.left) + 1

        if startNode.right is not None:
            right = self.__height__(startNode.right) + 1

        return max(left, right)

    def findParent(self, node):
        parent = self.header
        while True:
            if parent is None or parent.isParent(node): break
            elif  parent.value <= node.value: parent = parent.left
            else: parent = parent.right
            # if parent is None: break
        return parent


    def preorderWalk(self, startNode = None, fn = None):
        if startNode is None:
            startNode = self.header

        if fn is None:
            print startNode.value
        else:
            fn(startNode)

        if startNode.left is not None:
            self.preorderWalk(startNode.left)

        if startNode.right is not None:
            self.preorderWalk(startNode.right)

    def inorderWalk(self, startNode = None, fn = None):
        if startNode is None:
            startNode = self.header

        if startNode.left is not None:
            self.preorderWalk(startNode.left)

        if fn is None:
            print startNode.value
        else:
            fn(startNode)

        if startNode.right is not None:
            self.preorderWalk(startNode.right)

    def postorderWalk(self, startNode = None, fn = None):
        if startNode is None:
            startNode = self.header

        if startNode.left is not None:
            self.preorderWalk(startNode.left)

        if startNode.right is not None:
            self.preorderWalk(startNode.right)

        if fn is None:
            print startNode.value
        else:
            fn(startNode)

    def travel(self, startNode = None, height = 0, bcode = 0b0, fn = None):
        if startNode is None:
            if self.isEmpty: return
            startNode = self.header

        if fn is not None: fn(startNode, height, bcode)

        if startNode.left is not None:
            self.travel(startNode.left, height + 1, bcode << 1, fn)

        if startNode.right is not None:
            self.travel(startNode.right, height + 1, (bcode << 1) + 1, fn)

    def generateTreeDic(self):
        """
        将树转化为字典
        :return:
        """
        treeDic = [dict() for _ in range(self.height)]

        def travelFN(node, height, bcode):
            print bcode
            treeDic[height][str(bcode)] = node.value

        self.travel(fn=travelFN)

        return treeDic


    def storeTree(self, fp):
        """
        存储一棵树
        :param fp: 文件路径
        """
        treeDic = self.generateTreeDic()
        import json
        toFile = open(fp, "w")
        json.dump(treeDic, toFile)
        toFile.close()

    def generateTreeWithJSON(treeDic):
        """
        根据JSON生成树
        :param treeDic: JSON数据
        :return:
        """
        bTree = BTree()
        bTree.header = Node(treeDic[0]["0"])
        for height in range(1, len(treeDic)):
            layerNodes = treeDic[height]
            for col, v in zip(layerNodes.keys(), layerNodes.values()):
                # 获取col的二进制字符串
                huffmanCode = bin(int(col))[2:]

                # 补全赫夫曼编码
                for _ in range(height - len(huffmanCode)):
                    huffmanCode = '0' + huffmanCode

                # 将节点插入到树中
                node = Node(v)
                BTree.__addNodeWithHuffmanCode__(bTree, node, huffmanCode)

    def __addNodeWithHuffmanCode__(tree, node, huffmanCode):
        """ 添加节点到树种 """
        if tree.isEmpty:
            tree.header = node
            return

        curNode = tree.header
        index = 0
        while True:
            if index == len(huffmanCode) - 1:
                if huffmanCode[index] == 0:
                    curNode.left = node
                else:
                    curNode.right = node
                node.parent = curNode
            else:
                if huffmanCode[index] == 0:
                    curNode = curNode.left
                else:
                    curNode = curNode.right

            index += 1

    def loadTree(fp):
        """
        从文件中加载JSON数据并生成一棵树

        :param fp: 文件路径
        :return: BTree
        """
        import json
        treeDic = json.load(fp)
        return BTree.generateTreeWithJSON(treeDic)













