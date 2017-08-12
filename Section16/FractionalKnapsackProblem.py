# -*- coding: utf-8 -*-

def solveFractionalKnapsackProblem(V, W, weight):
    """分数背包问题
    贪心算法
    已按价值排好序
    :param V: 价值
    :param W: 重量
    :param weight: 背包能承受的最大重量
    :return: 选择的价值
    """
    curWeight = 0
    p = []
    for index in range(len(V)):
        if curWeight + W[index] > weight:
            v = (weight - curWeight) * V[index] / W[index] * 1.0
            p.append(v)
            break
        else:
            v = V[index]
            p.append(v)
        curWeight += W[index]
    return p

if __name__ == '__main__':
    V = [60, 100, 120]
    W = [10, 20, 30]
    values = solveFractionalKnapsackProblem(V, W, 50)
    print "总价值: ", sum(values)
    print "选取的价值: ", values














