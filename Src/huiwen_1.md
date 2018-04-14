## 回文序列
****
- **题目描述**：
> 现在给出一个数字序列，允许使用一种转换操作：
>
>     选择任意两个相邻的数，然后从序列移除这两个数，并用这两个数字的和插入到这两个数之前的位置(只插入一个和)。现在对于所给序列要求出最少需要多少次操作可以将其变成回文序列。
> 输入描述:
>
>     输入为两行，第一行为序列长度n ( 1 ≤ n ≤ 50) 第二行为序列中的n个整数item[i] (1 ≤ iteam[i] ≤ 1000)，以空格分隔。
> 输出描述:
>
>     输出一个数，表示最少需要的转换次数
- **分析**：
> 首尾指针跟踪;
> 两个数不相等就进行加法：小的数加上相邻的值
- **Python代码实现：**
```Python
# -*- coding:utf-8 -*-
"""
链接：https://www.nowcoder.com/questionTerminal/0147cbd790724bc9ae0b779aaf7c5b50
来源：牛客网

现在给出一个数字序列，允许使用一种转换操作：
选择任意两个相邻的数，然后从序列移除这两个数，并用这两个数字的和插入到这两个数之前的位置(只插入一个和)。
现在对于所给序列要求出最少需要多少次操作可以将其变成回文序列。
输入描述:
     输入为两行，第一行为序列长度n ( 1 ≤ n ≤ 50) 第二行为序列中的n个整数item[i] (1 ≤ iteam[i] ≤ 1000)，以空格分隔。
输出描述:
     输出一个数，表示最少需要的转换次数
解决方法：
#首尾指针跟踪
#两个数不相等就进行加法：小的数加上相邻的值
"""


def huiwen(lst, head, tail):
    left = lst[head]
    right = lst[tail]
    num = 0
    while head < tail:
        if left < right:
            head += 1
            left += lst[head]
            num += 1
        elif left > right:
            tail -= 1
            right += lst[tail]
            num += 1
        else:
            head += 1
            tail -= 1
            left = lst[head]
            right = lst[tail]
    return num
if __name__ == "__main__":
    n = int(input().strip())
    ary = [int(i) for i in input().strip().split()]
    print(huiwen(ary, 0, n-1))

```
*****
