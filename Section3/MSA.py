# -*- coding: utf-8 -*-


def maxSubArray(arr):
    '''
    求最大子数组，时间复杂度O(n^2)

    首先先确定数组大哪一个位置出现小于或等于0， 在此过程中需要记录出现负值的位置
    如果小于等于0，则从后开始遍历记录负值的位置，在求和和之前最大的比较
    知道数组最后一个元素

    例如: [1, 2, -2, 1, -3] (位置从0开始)
    1 + 2 - 2 + 1 -3 = -1 < 0
    此时应该回溯到位置为3的位置再求和 1 + 2 - 2 + 1 = 2， 即目前为最大
    再回溯到位置为1的位置再求和 1 + 2 = 3 > 2 即目前最大
    由于再向前没有负值，所以最大即为(0, 1, 3)

    优化: 在每次记录负数出现时，可以把当前的和进行存储，可避免回溯时重复计算

    :param arr: 数组
    :return: (start, end, total)
    '''
    arrLength = len(arr)
    maxArr = (0, 0, arr[0])
    criticals = [] # 临界点，记录负值出现的位置
    total = 0
    preIndex = 0
    for index in range(arrLength):
        cv = arr[index]
        total += cv

        if total <= 0 or index == arrLength - 1:
            # 最后一个是否小于0
            if cv < 0 and index == arrLength - 1: criticals.append(index)

            # 从preIndex开始是否都是正数，且和大于preIndex之前的最大值子数组之和
            if cv >= 0 and total > maxArr[2] and len(criticals) == 0 and index == arrLength - 1: return (preIndex, arrLength - 1, total)

            # 使用临界区回溯求最大值
            while True:
                criticalLength = len(criticals)
                if criticalLength == 0: break
                lastValue = criticals.pop(criticalLength - 1)
                if preIndex == lastValue:
                    sectionSum = arr[preIndex]
                else:
                    sectionSum = sum(arr[preIndex : lastValue])
                if sectionSum > maxArr[2]:
                    maxArr = (preIndex, lastValue - 1, sectionSum)

            total = 0
            preIndex = index + 1
        elif cv <= 0:
            criticalLength = len(criticals)
            if criticalLength == 0 or criticalLength > 0 and index - criticals[criticalLength - 1] != 1:
                criticals.append(index)

    return maxArr


if __name__ == "__main__":
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print maxSubArray(arr)











