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
