# -*- coding: utf-8 -*-

"""贪心算法

活动选择
"""

def activitySelect(activities):
    op = [activities[0]]

    for index in range(1, len(activities)):
        if op[len(op) - 1][1] <= activities[index][0]:
            op.append(activities[index])

    return op

if __name__ == '__main__':
    # 活动已经按结束时间进行排序
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11),
                  (8, 12), (2, 14), (12, 16)]

    print activitySelect(activities)











