# -*- coding:utf-8 -*-
# 希尔排序：
"""
原理：它的另一个名字是“递减增量排序算法“。这个算法可以看作是插入排序的优化版，
    因为插入排序需要一位一位比较，然后放置到正确位置。
    为了提升比较的跨度，希尔排序将数组按照一定步长分成几个子数组进行排序，
    通过逐渐减短步长来完成最终排序。
步骤：
    1.计算当前步长，按步长划分子数组
    2.子数组内插入排序
    3.步长除以2后继续12两步，直到步长最后变成1
从小到大排序
"""


def shell_sort(lst):
    n = len(lst)
    gap = n >> 1  # 初始步长,拆分两列
    if n == 0:
        return []
    while gap > 0:
        for i in range(gap, n):  # 对每一列进行插入排序，从gap -> n
            temp = lst[i]
            j = i - gap
            while j >= 0 and lst[j] > temp:  # 插入排序eg:[1,2,3,5]中插入4
                lst[j + gap] = lst[j]  # 将较大值交换给后面位置
                j -= gap
            lst[j + gap] = temp  # 满足条件之后即塞入
        gap >>= 1  # 重新设置步长
    return lst


def main():
    print(shell_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
