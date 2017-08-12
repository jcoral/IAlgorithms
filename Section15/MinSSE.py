# -*- coding: utf-8 -*-
import numpy as np
import random

def makeRange(k, start, end, splitChr = "-"):
    """
    根据开始的位置和结束的位置返回一个范围字符串
    :param start: 开始的位置
    :param end:   结束的位置
    :return:      str
    """
    return str(k) + ":" + str(start) + splitChr + str(end)

bp = {}
def calMinSSE(A, k, start = 0, end = None):
    """ 求怎样分割A为k段使得SSE最小
    下标从1开始
    思想: 设分为k段, 给定不等式 1 <= i <= m <= j <= n,
         则只需要求min(var([A(i) ... A(m)]) + f([A(m) ... A(j)], k - 1))

    :param A: 原数组
    :param k: 分为几段
    :param start: 开始的位置
    :param end:   结束的位置
    :return:      minSSE
    """
    if end is None: end = len(A) - 1
    if k == 1:
        bp[makeRange(k, start, end)] = (-1, np.var(A[start: end + 1]))
        return np.var(A[start: end + 1])
    minSSE = None
    opPosition = -1
    for index in range(start, end):
        # 求前半部分的方差
        frontSection = np.var(A[start: index + 1])

        # 若条件成立则说明在剩余的部分不能够分为k段，则退出
        if end - index + 1 < k: break

        # 求后半部分的方差
        if bp.__contains__(makeRange(k - 1, index + 1, end)):
            backSection = bp[makeRange(k - 1, start + 1, end)][1]
        else:
            backSection = calMinSSE(A, k - 1, index + 1, end)
        if backSection is None: backSection = 0

        # 计算SSE
        sse = frontSection + backSection
        if minSSE is None or sse < minSSE:
            minSSE = sse
            opPosition = index

    bp[makeRange(k, start, end)] = (opPosition, minSSE)
    return minSSE

def output(A, k):
    """
    输出分割完的数组
    :param A: 数组
    :param k: 几段
    """
    start = 0
    end = len(A) - 1
    while True:
        print '[',
        curCutPosition = bp[makeRange(k, start, end)][0]

        if curCutPosition == -1: curCutPosition = end
        for index in range(start, curCutPosition + 1):
            print A[index],
            if index != curCutPosition: print ", ",

        start = curCutPosition + 1
        k -= 1
        print ']',
        if k == 0: break


if __name__ == '__main__':
    a = [random.randint(0, 10) for _ in range(10)]
    print "Origin: ", a
    print "MinSSE: ", calMinSSE(a, 4)
    output(a, 4)








