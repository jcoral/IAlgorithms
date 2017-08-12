# -*- coding: utf-8 -*-


def maxSubArray(arr):
    """
    求最大子数组

    首先先确定数组大哪一个位置出现小于或等于0， 在此过程中需要记录出现负值的位置
    如果小于等于0，则从后开始遍历记录负值的位置，在求和与之前最大的比较
    知道数组最后一个元素

    例如: [1, 2, -4, 1, -3] (位置从0开始)
    1 + 2 - 4 = -1 < 0
    在此序列中找到最大子数组为 (0, 1, 3)
    1 - 3 = -2 < 0
    在此序列中再到最大子数组为 (3, 3, 1)

    所以最大子数组为 (0, 1, 3)

    :param arr: 数组
    :return: (start, end, total)
    """
    arrLength = len(arr)
    maxArr = (0, 0, arr[0])
    total = 0
    preIndex = 0
    sectionSumMaxValue = None
    sectionSumMaxIndex = 0
    for index in range(arrLength):
        cv = arr[index]
        total += cv

        if total <= 0 or index == arrLength - 1:
            if sectionSumMaxValue > maxArr[2]:
                maxArr = (preIndex, sectionSumMaxIndex, sectionSumMaxValue)

            total = 0
            preIndex = index + 1

        elif cv >= 0 and sectionSumMaxValue == None or total > sectionSumMaxValue:
            sectionSumMaxValue = total
            sectionSumMaxIndex = index

        if cv >= 0 and total > maxArr[2] and sectionSumMaxIndex == index == arrLength - 1: return (preIndex, arrLength - 1, total)

    return maxArr


if __name__ == "__main__":
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print maxSubArray([1, 2, -4, 1, -3])











