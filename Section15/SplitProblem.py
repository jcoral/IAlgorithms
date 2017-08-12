# -*- coding: utf-8 -*-

import random
p = random.sample(range(1, 10000), 500)
p.sort()

bp = {} # 存放已经计算过的值

"""
[n: position]: 存放每一段的最优分割位置

EG: 假设其值为{1: 1, 2: 1, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3}

求解n为8的分割位置

则先分为3段， 剩余还有5
剩下的即为n=5时的分割问题， 则分为3， 剩余2
剩余的即为n=2时的分割问题， 则为为1段， 剩余1

所以最终的分割问题为5, 3, 1, 1
"""
cutPosition = {}

def splitLine(n):
    """
    分割钢管以获取最大利润

    EG: 假设n = 4，将需要进行以下情况进行分割, 在求解index = v时需要递归的求解后半部分子问题的最优解

    index = 1
    —— ——————
    —— —— —— ——
    —— —— ————
    —— ———— ——

    index = 2
    ———— —— ——
    ———— ————

    index = 3
    ———————— ——

    index = 4
    ————————

    :param n: 长度
    :return: 当前长度的最大值
    """

    maxValue = None
    maxPosition = None
    if n <= 0:
        return 0

    for index in range(1, n + 1):
        subp = 0
        if bp.__contains__(n - index):
            subp = bp[n - index]
        else:
            subp = splitLine(n - index)

        subp += p[index - 1]
        if subp >= maxValue:
            maxValue = subp
            maxPosition = index

    cutPosition[n] = maxPosition
    bp[n] = maxValue
    return maxValue


if __name__ == '__main__':
    sn = 15
    print "Weight: ", p[: sn]
    print "Optimal: ", splitLine(sn)
    s = []
    while True:
        r = cutPosition[sn]
        s.append(r)
        sn = sn - r
        if sn <= 0: break

    print "Cut position: ", s



