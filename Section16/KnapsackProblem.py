# -*- coding: utf-8 -*-

def makeRange(weight, n, splitChr = ":"):
    """
    :param weight: 开始的位置
    :param n:      结束的位置
    :return:       str
    """
    return str(weight) + splitChr + str(n)

bp = {}
def solveKnapsackProblem(V, W, weight, start = 0):
    """
    下标从1开始
    i ∈ [1 ... n]
    设ai ∈ {0， 1}
    则有 ∑(ai Wi) <= W, max(∑ai Vi)

    :param V: 价值
    :param W: 重量
    :param weight: 背包最大承受的重量
    :param start:  开始的位置， 在start之前的东西将会忽略
    :return: 总价值
    """
    if weight <= 0: return 0
    op = 0
    position = -1
    for index in range(start, len(V)):
        if bp.__contains__(makeRange(weight - W[index], index + 1)):
            v0 = bp[makeRange(weight - W[index], index + 1)][1]
        else:
            v0 = solveKnapsackProblem(V, W, weight - W[index], index + 1)

        if V[index] + v0 > op and W[index] <= weight:
            op = V[index] + v0
            position = index

    bp[makeRange(weight, start)] = (position, op)
    return op

def output(V, W, weight):
    curPosition = -1
    freeWeight = weight
    while True:
        curPosition = bp[makeRange(freeWeight, curPosition + 1)][0]
        print V[curPosition],
        freeWeight -= W[curPosition]
        if freeWeight <= 0: break


if __name__ == '__main__':
    V = [21, 123, 4, 234, 1231, 454]
    W = [2, 3, 1, 4, 6, 5]
    print "总价值: ", solveKnapsackProblem(V, W, 7)
    print "选取的价值: ",
    output(V, W, 7)








