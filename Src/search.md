## 查找算法
1. **有序数组中数字出现的次数**
2. **数组中出现次数超过一半的数字**
***
#### 1.有序数组中数字出现的次数
* 题目描述：
  >在给定的一个已经排好序的数组中，找出指定数字出现的次数。例如数组[1,2,3,4,4,4,4,6,8,9]中4出现的次数为4次
* 思路与方法：
  >此问题可以在二分法的基础上进行改进。假设数组a为递增的数列，需要查找的数字为num，
  >可以分别查找num在数组a中出现的起始位置和最后一次的位置，通过二者的差计算出数字num在数组a中出现的次数。
* Python代码实现：
```Python
# -*- coding:utf-8 -*-
def findcountofnum(a, num, isleft):  # 查找指定数字在有序数组中出现的次数，isLeft标记最左和最右
    pleft = 0
    pright = len(a) - 1
    #  二分查找区间[left, right]
    while pleft <= pright:
        mid = pleft + ((pright - pleft) >> 1)  # 防止溢出，移位也更高效。同时，每次循环都需要更新
        if a[mid] < num:  # 后半段查找
            pleft = mid + 1
        elif a[mid] > num:  # 前半段查找
            pright = mid - 1
        else:  # 相等情况
            pos = mid  # 记录相等下标位置
            if isleft:  # 查找最左值
                pright = mid - 1
            else:  # 查找最右值
                pleft = mid + 1
    return pos


if __name__ == "__main__":
    a = [1, 2, 3, 4, 4, 4, 4, 6, 6, 9]
    num = 9
    left = findcountofnum(a, num, True)
    right = findcountofnum(a, num, False)
    print("count of number %s: %s" % (num, right - left + 1))

```
**参考资料：**
>* [二分法计算有序数组中数字出现的次数](https://blog.csdn.net/jeanphorn/article/details/46351475)
***
#### 2.数组中出现次数超过一半的数字
* 题目描述:
  >数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字
* 分析:
  > 根据数组组特点找出O(n)的算法
  > 数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。因此我们可以考虑在遍历数组的时候保存两个值：
  > 一个是数组中的一个数字， 一个是次数。当我们遍历到下～个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加l ：如果下一个数字和我们之前 
  > 保存的数字，不同，则次数减1 。如果次数为霉，我们需要保存下一个数字，并把次数设为1 。由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要
  > 多，那么要找的数字肯定是最后一次把次数设为1 时对应的数字。
* Python代码实现：
```Python
# -*- coding: utf-8 -*-
#
"""
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字
分析：
采用阵地攻守的思想：
第一个数字作为第一个士兵，守阵地；count = 1；
遇到相同元素，count++;
遇到不相同元素，即为敌人，同归于尽,count--；当遇到count为0的情况，又以新的i值作为守阵地的士兵，继续下去，到最后还留在阵地上的士兵，有可能是主元素。
再加一次循环，记录这个士兵的个数看是否大于数组一般即可
"""


def morethanhalfnum(a):
    if len(a) == 0:
        print('invalid input!')
        return
    result = a[0]
    count = 1
    cnt = 0
    for i in range(1, len(a)):
        if a[i] == result:
            count += 1
        else:
            count -= 1
        if count == 0:
            result = a[i]
            count = 1
    for j in range(len(a)):
        if a[j] == result:
            cnt += 1
    if cnt << 1 >= len(a):
        return result
    else:
        print("invalid input!")


if __name__ == "__main__":
    ary = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(morethanhalfnum(ary))

```
**参考资料：**
>* [数组中出现次数超过一半的数字](https://www.nowcoder.com/questionTerminal/e8a1b01a2df14cb2b228b30ee6a92163?source=relative)

***
