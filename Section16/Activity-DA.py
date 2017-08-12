# -*- coding: utf-8 -*-

"""动态规划

活动选择
"""

bp = {}
def activitySelect(activities, i = 0):
    op = None
    for index in range(i, len(activities)):
        subActivities = [] # 存放子活动的时间

        # 查找下一个与当前活动兼容的活动
        for j in range(index + 1, len(activities)):
            if activities[j][0] >= activities[index][1]:
                if bp.__contains__(j):
                    subActivities = bp[j]
                    break
                else:
                    subActivities = activitySelect(activities, j)
                    break

        if op is None or len(op) < len(subActivities) + 1:
            op = [activities[index]] + subActivities

    bp[i] = op
    return op

if __name__ == '__main__':
    # 以根据结束时间进行排序
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11),
                  (8, 12), (2, 14), (12, 16)]

    print activitySelect(activities)










