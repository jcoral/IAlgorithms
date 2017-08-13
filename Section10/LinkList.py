# -*- coding: utf-8 -*-

class LinkNode:
    def __init__(self, v):
        self.next = None
        self.value = v

class LinkList:

    def __init__(self):
        self.header = LinkNode(None)
        self.next = None

    def add(self, node):
        curNode = self.header
        while True:
            if curNode.next is None:
                curNode.next = node
                return
            else:
                curNode = curNode.next

    def insert(self, node):
        node.next = self.header.next
        self.header.next = node










