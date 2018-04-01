# -*- coding:utf-8 -*-
# 快速排序：
"""
原理：快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，
而且快排采用了分治法的思想，所以在很多笔试面试中能经常看到快排的影子。
可见掌握快排的重要性。

步骤：
1.从数列中挑出一个元素作为基准数。
2.分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3.再对左右区间递归执行第二步，直至各区间只有一个数。

"""


def quick_sort(array):
    return q_sort(array, 0, len(array) - 1)


def q_sort(array, left, right):  # 快排函数，array为待排序数组，left为待排序的左边界，right为右边界
    if left >= right:
        return array
    k = array[left]  # 取最左边卫基准值
    lp, rp = left, right  # 左右指针
    while lp < rp:
        while array[rp] >= k and lp < rp:  # 与基准值K比较
            rp -= 1
        while array[lp] <= k and lp < rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]  # 交换右边小的和左边大的
    array[left], array[lp] = array[lp], array[left]  # 交换指针，更新新的基准值K
    q_sort(array, left, lp - 1)  # 左边递归快排
    q_sort(array, rp + 1, right)  # 右边递归快排
    return array


def main():
    print(quick_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
