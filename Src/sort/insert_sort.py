# -*- coding:utf-8 -*-
# 插入排序：
"""
原理：从左到右，把选出的一个数和前面的数进行比较，找到最适合它的位置放入，
      使前面部分有序
步骤：
    1.从左开始，选出当前位置的数x，和它之前的数y比较，如果x < y则交换两者
    2.对x之前的数都执行1步骤，直到前面的数字都有序
    3.选择有序部分后一个数字，插入到前面有序部分，直到没有数字可选择
从小到大排序
"""


def insert_sort(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return []
    for i in range(1, lst_len):
        for j in range(i, 0, -1):  # 比较之前的i个数据，交换小的到前面
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


def main():
    print(insert_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
