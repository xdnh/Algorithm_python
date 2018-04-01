# -*- coding:utf-8 -*-
# 归并排序：
"""
原理：是采用分治法（Divide and Conquer）的一个典型例子。
    这个排序的特点是把一个数组打散成小数组，然后再把小数组拼凑再排序，
    直到最终数组有序
步骤：
    1.把当前数组分化成n个单位为1的子数组，然后两两比较合并成单位为2的n/2个子数组
    2.继续进行这个过程，按照2的倍数进行子数组的比较合并，直到最终数组有序
从小到大排序

归并排序是采用分治法的一个非常典型的应用。
归并排序的思想就是先递归分解数组，再合并数组。

先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，
取了后相应的指针就往后移一位。
然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

再考虑递归分解，基本思路是将数组分解成left和right，
如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。
如何让这两个数组内部是有序的？
可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。
然后合并排序相邻二个小组即可。
"""


def merge_sort(lst):  # 先递归分解数组
    if len(lst) <= 1:
        return lst
    num = len(lst) >> 1  # 二分分解
    left = merge_sort(lst[:num])
    right = merge_sort(lst[num:])
    return merge(left, right)  # 合并数组


def merge(left, right):  # 将两个有序数组left[]和right[]合并成一个大的有序数组
    ary = []
    l, r = 0, 0  # left与right数组的下标指针
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ary.append(left[l])
            l += 1
        else:
            ary.append(right[r])
            r += 1
    ary += left[l:]
    ary += right[r:]
    return ary


def main():
    print(merge_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
