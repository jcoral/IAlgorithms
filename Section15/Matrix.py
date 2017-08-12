# -*- coding: utf-8 -*-

"""查找矩阵计算乘法最少次数

算法思想: 设用A(m)表示一个矩阵, n为矩阵的个数, k ∈ [i, j], 其中0 <= i <= j <= n
则需要计算optimal(A(i) ... A(k)) ∪ optimal(A(k + 1) ... A(j))

设A = abcde(a, b, c, d, e为矩阵并且可相乘)
则有
1> optimal(a) ∪ optimal(bcde)
   1.1> optimal(b) ∪ optimal(cde)
        1.1.1> optimal(c) ∪ optimal(de)
               1.1.1.1> optimal(d) ∪ optimal(e)
        1.1.2> optimal(cd) ∪ optimal(e)
   1.2> optimal(bc) ∪ optimal(de)
        1.2.1> optimal(d) ∪ optimal(e)
......

n> optimal(abcd) ∪ optimal(e)

"""


def multMatrix(m1, m2):
    """
    计算两个矩阵相乘
    :param m1: 矩阵1
    :param m2: 矩阵2
    :return: (matrix, times)
    """
    return ((m1[0], m2[1]), m1[0] * m1[1] * m2[0] * m2[1])

def makeRange(start, end, splitChr = "-"):
    """
    根据开始的位置和结束的位置返回一个范围字符串
    :param start: 开始的位置
    :param end:   结束的位置
    :return:      str
    """
    return str(start) + splitChr + str(end)

def matrixMult(A, bp, start = 0, end = None):
    """
    计算矩阵

    :param A:     矩阵链
    :param bp:    备份已经计算过的子问题
    :param start: 子问题开始的位置
    :param end:   子问题结束的位置
    :return: (position, times, matrix)
    """
    if end is None:
        end = len(A) - 1
    if start == end:
        return (-1, 0, A[start])

    # 保存当前最优结果
    op = (-1, None, None) # (position, times, matrix)
    for index in range(start, end):
        # 前部分
        if bp.__contains__(makeRange(start, index)):
            hm = bp[makeRange(start, index)]
        else:
            hm = matrixMult(A, bp, start, index)

        # 后部分
        if bp.__contains__(makeRange(index + 1, end)):
            fm = bp[makeRange(index + 1, end)]
        else:
            fm = matrixMult(A, bp, index + 1, end)

        # 计算两个矩阵
        curMatrix = multMatrix(hm[2], fm[2])

        # 当前分割的乘法总次数
        curTimes  = fm[1] + hm[1] + curMatrix[1]

        if op[1] is None or op[1] > curTimes:
            op = (index, curTimes, curMatrix[0])

    # 不做拆分进行计算的次数
    matrixAndTimes = (A[start], 0)
    curTimes  = 0
    for index in range(start + 1, end+ 1):
        matrixAndTimes = multMatrix(matrixAndTimes[0], A[index])
        curTimes += matrixAndTimes[1]

    if curTimes <= op[1]:
        op = (-1, curTimes, matrixAndTimes[0])

    bp[makeRange(start, end)] = op
    return op

def outputResult(A, bp):
    """
    输出矩阵
    :param A:
    :param bp:
    """
    def makeString(start, end):
        if start == end:
            print start,
            return
        print "(",
        ptm = bp[makeRange(start, end)]
        if ptm[0] == -1:
            print str(start) + " - " + str(end),
        else:
            makeString(start, ptm[0])    # 前半部分
            makeString(ptm[0] + 1, end)  # 右半部分
        print ")",

    makeString(0, len(A) - 1)

def matrixChainOrder(A):
    #[range: (position, times, matrix)] 存放已经计算过的子问题
    bp = dict()
    matrixMult(A, bp)
    outputResult(A, bp)


if __name__ == '__main__':
    A = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    matrixChainOrder(A)








