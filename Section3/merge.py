# -*- coding: utf-8 -*-

import random
import math

def generateArray(length):
    return [random.randint(0, 1000) for _ in range(length)]


def binarySearch(arr, value, start = 0, end = None):
    """
    二分查找
    :param arr:   需要查找的数组
    :param value: 需要查找的值
    :param start: 起始位置
    :param end:   结束位置
    :return:      如结果为正，则表示存在当前值；若为负，则value大于前一个，小于后一个
    """
    if end == None: end = len(arr) - 1
    mid = start + math.floor((end - start) / 2)
    while True:
        midValue = arr[int(mid)]
        if midValue == value:
            return mid
        elif midValue < value:
            # 左边
            start = mid
            mid = start + math.ceil((end - start) / 2)
        elif midValue > value:
            # 右边
            if mid == end: break
            end = mid
            mid = start + math.floor((end - start) / 2)
        if start == end: break
    return -mid


def mergeMain(arr):
    """
    归并排序
    :param arr: 数组
    :return:    排序好的数组
    """
    deep = 0
    arrLength = len(arr)
    while True:
        # 每一块的大小
        width = 2 ** deep

        # 块的总数
        sectionLength = math.ceil(arrLength / width)

        if width >= arrLength: return arr

        # 合并所有的块
        for section in range(0, int(sectionLength), 2):
            # 对两个块进行合并
            if section > sectionLength: break
            startIndex = section * width
            for backSectionIndex in range((section + 1) * width, (section + 2) * width):
                if backSectionIndex >= len(arr): break
                index = int(math.fabs(binarySearch(arr, arr[backSectionIndex], startIndex, backSectionIndex - 1)))
                if arr[backSectionIndex] > arr[index]: continue
                startIndex = index
                value = arr.pop(backSectionIndex)
                arr.insert(int(math.fabs(index)), value)

        if sectionLength <= 1: return arr
        deep += 1


if __name__ == "__main__":
    for _ in range(10):
        arr = generateArray(10)
        print arr
        arr = mergeMain(arr)
        print arr


