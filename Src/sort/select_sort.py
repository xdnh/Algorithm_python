# -*- coding:utf-8 -*-
# 选择排序：
"""
原理：每次都从乱序数组中找到最大（最小）值，放到当前乱序数组头部，最终使数组有序
步骤：
    1.从左开始，选择后面元素中最小值，和最左元素交换
    2.从当前已交换位置往后执行，直到最后一个元素
从小到大排序
"""


def selection_sort(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return []
    for i in range(lst_len - 1):
        small_val = lst[i]
        index = i
        for j in range(i + 1, lst_len):
            if lst[j] < small_val:
                small_val = lst[j]
                index = j
        lst[i], lst[index] = lst[index], lst[i]
    return lst


def main():
    print(selection_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
