# -*- coding: utf-8 -*-
import random

import time


from Section12.BSTree import BSTree
from Section12.Node import Node

l = [random.randint(0, 1000000) for _ in range(20)]
l = [5,2,80,67, 60, 59,123,4,1]
# l = [1, 2, 3, 123, 123, 1, 231, 123, 12, 123, 23, 13]

""" 排序和建树进行时间的比较
print time.time()
tree = BSTree()

for v in l:
    tree.addChild(v)

# tree.preorderWalk()

print time.time(), "\n--- End ---"

l.sort()

print time.time()
"""


""" 查找的时间对比

from Section3.merge import binarySearch
tree = BSTree()

for v in l:
    tree.addChild(v)
l.sort()

print time.time()
tree.find(l[234])

print time.time()

binarySearch(l, l[234])
print time.time()
"""

tree = BSTree()
nodes = []
for v in l:
    nodes.append(Node(v))
    tree.addChild(v)

""" 删除一个节点 """
tree.preorderWalk()
tree.removeNode(tree.header)
print
tree.preorderWalk()
# tree.storeTree("tree.json")
# print tree.findParent(tree.header.left.right)

""" 赫夫曼树 """
print
from HuffmanTree import HuffmanTree
ht = HuffmanTree(nodes)
ht.preorderWalk()





