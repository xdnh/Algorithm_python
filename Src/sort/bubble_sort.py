# -*- coding:utf-8 -*-
# 冒泡排序：
"""
原理：每次从左到右两两比较，把大的交换到后面，
      每次可以确保将前M个元素的最大值移动到最右边
      从小到大排序
"""


# 法1：每趟排序做做多次交换(<(n-i-1))
def bubble_sort1(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return []
    for i in range(lst_len-1):
        for j in range(lst_len-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# 法2:每趟只做一次交换，将最小值交换到第i个位置
def bubble_sort2(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return []
    for i in range(lst_len-1):
        small_val = lst[i]  # 第i趟排序的最小值
        index = i  # 第i趟排序的最小值的索引
        for j in range(i+1, lst_len):
            if small_val > lst[j]:
                small_val = lst[j]
                index = j
        lst[i], lst[index] = lst[index], lst[i]  # 将最小值依次交换给第i个位置
    return lst


def main():
    print(bubble_sort1([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
