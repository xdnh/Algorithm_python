## 动态规划算法解LCS问题


****
#### 最长公共子序列
* 题目描述：
>- 题目：如果字符串一的所有字符按其在字符串中的顺序出现在另外一个字符串二中，则字符串一称之为字符串二的子串。
>- 注意: 并不要求子串（字符串一）的字符必须连续出现在字符串二中。
>请编写一个函数，输入两个字符串，求它们的最长公共子串，并打印出最长公共子串。
>- 例如：输入两个字符串BDCABA和ABCBDAB，字符串BCBA和BDAB都是是它们的最长公共子序列，则输出它们的长度4，并打印任意一个子序列。
* 分析：
>- Xi=﹤x1，⋯，xi﹥即X序列的前i个字符 (1≤i≤m)（前缀）
>- Yj=﹤y1，⋯，yj﹥即Y序列的前j个字符 (1≤j≤n)（前缀）
>- 假定Z=﹤z1，⋯，zk﹥∈LCS(X , Y)。
1. 若xm=yn（最后一个字符相同），则不难用反证法证明：该字符必是X与Y的任一最长公共子序列Z（设长度为k）的最后一个字符，即有zk = xm = yn 且显然有Zk-1∈LCS(Xm-1 , Yn-1)即Z的前缀Zk-1是Xm-1与Yn-1的最长公共子序列。此时，问题化归成求Xm-1与Yn-1的LCS（LCS(X , Y)的长度等于LCS(Xm-1 , Yn-1)的长度加1）。
2. 若xm≠yn，则亦不难用反证法证明：要么Z∈LCS(Xm-1, Y)，要么Z∈LCS(X , Yn-1)。由于zk≠xm与zk≠yn其中至少有一个必成立，若zk≠xm则有Z∈LCS(Xm-1 , Y)，类似的，若zk≠yn 则有Z∈LCS(X , Yn-1)。此时，问题化归成求Xm-1与Y的LCS及X与Yn-1的LCS。LCS(X , Y)的长度为：max{LCS(Xm-1 , Y)的长度, LCS(X , Yn-1)的长度}。
* 递归关系如下：
> ![lcs_1](https://github.com/xdnh/Algorithm_python/raw/master/pic/lcs_1.gif)
* Python 代码实现
> 整个过程中表c和b的内容如下图所示:
>> ![lcs](https://github.com/xdnh/Algorithm_python/raw/master/pic/lcs.png)
```Python
# -*- coding:utf-8 -*-
"""
最长公共子序列。
题目：如果字符串一的所有字符按其在字符串中的顺序出现在另外一个字符串二中，
则字符串一称之为字符串二的子串。

注意，并不要求子串（字符串一）的字符必须连续出现在字符串二中。
请编写一个函数，输入两个字符串，求它们的最长公共子串，并打印出最长公共子串。
例如：输入两个字符串BDCABA和ABCBDAB，字符串BCBA和BDAB都是是它们的最长公共子序列，则输出它们的长度4，并打印任意一个子序列。

分析：求最长公共子序列（Longest Common Subsequence, LCS）是一道非常经典的动态规划题.
"""


def lcs_length(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    c = [[0 for j in range(n+1)] for i in range(m+1)]  # c[i][j]存储Xi和Yj的最长公共子序列的长度
    # b = [[0 for i in range(m)] for j in range(n)]  # b[i][j]记录指示c[i][j]的值是由哪个问题解决的
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if lst1[i-1] == lst2[j-1]:  # xm=yn，则zk=xm=yn且Zk-1是Xm-1和Yn-1的最长公共子序列
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:  # xm≠yn且zk≠xm ，则Z是Xm-1和Y的最长公共子序列
                c[i][j] = c[i-1][j]
            else:   # xm≠yn且zk≠y，则Z是X和Yn-1的最长公共子序列
                c[i][j] = c[i][j-1]
    return c


def printlcs(c, x, i, j):
    if i == 0 or j == 0:
        return
    if c[i][j] == c[i-1][j]:  # 向上顺序
        printlcs(c, x, i-1, j)
    elif c[i][j] == c[i][j-1]:  # 向左顺序
        printlcs(c, x, i, j-1)
    else:  # 左上顺序（左上>向上>向左）
        printlcs(c, x, i-1, j-1)
        print(x[i-1])


if __name__ == "__main__":
    x_i = list("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA")
    y_j = list("GTCGTTCGGAATGCCGTTGCTCTGTAAA")
    # x_i = list("ABCBDAB")
    # y_j = list("BDCABA")
    m, n = len(x_i), len(y_j)
    c = lcs_length(x_i, y_j)
    printlcs(c, x_i, m, n)

```


***
