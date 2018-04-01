# -*- coding:utf-8 -*-
# 堆排序（Heap Sort）：
"""
堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，
虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。

二叉堆具有以下性质：
    1.父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
    2每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。
在了解算法之前，首先了解在一维数组中节点的下标：
    1.i节点的父节点 parent(i) = floor((i-1)/2)
    2.i节点的左子节点 left(i) = 2i + 1
    3.i节点的右子节点 right(i) = 2i + 2
步骤：
    1.构造最大堆（Build_Max_Heap）：
若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆
。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的
左右子树都已经是大根堆。

    2.堆排序（HeapSort）：
由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。
因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。
第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。
第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。
重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，
故操作完后整个数组就是有序的了。

    3.最大堆调整（Max_Heapify）：
该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远
小于父节点 。
"""


def heap_sort(array):
    n = len(array)
    # 构造最大堆
    # first：从下往上第一个父节点
    first = len(array) >> 1 - 1  # n/2开始的元素均为大根堆（叶子结点）,
    for start in range(first, -1, -1):  # 反向构造大根堆
        max_heapify(array, start, n - 1)
    # 堆排序
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]  # 交换，依次移除根节点
        max_heapify(array, 0, end - 1)
    return array


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(array, start, end):
    root = start  # 根节点
    while True:
        child = root * 2 + 1
        if child > end:
            break  # 判断孩子结点是否存在
        if child + 1 < end and array[child] < array[child + 1]:  # 判断右结点是否存在，
            child += 1  # 取左右结点最大的结点以跟root结点比较
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]  # 比较交换最大值给root结点
            root = child
        else:
            break


def main():
    print(heap_sort([2, 1, 3, 0, 3837, 1, 33, 464]))


if __name__ == "__main__":
    main()
