## 动态规划实例

* 绝地求生捡装备（三级头三级甲）
***
#### 绝地求生捡装备（三级头三级甲）
* 题目描述：
  >绝地求生游戏捡装备，头盔（1, 2, 3级），衣服（1，2,3级）
  >初始状态记为（0， 0），问：捡到状态为（3， 3）的方法有多少种？
* 分析：
  >这是一道动态规划的问题。可以将此转化成4*4的二维数组，dp[i][j]表示到达状态（i, j）所走的路数
* Python代码实现
```Python
# -*- coding:utf-8 -*-
"""
题目描述：
绝地求生游戏捡装备，头盔（1, 2, 3级），衣服（1，2,3级）
初始状态记为（0， 0），问：捡到状态为（3， 3）的方法有多少种？
分析：
这是一道动态规划的问题。可以将此转化成4*4的二维数组，dp[i][j]表示到达状态（i, j）所走过的路数
"""

def juedipickequipment(raw, col):  # 4 x 4
    dp = [[0 for i in range(col)] for j in range(raw)]  # 定义一个4 x 4 的二维空白list
    dp[0][0] = 1  # 初始状态
    for i in range(raw):
        for j in range(col):
            for m in range(i):
                dp[i][j] += dp[m][j]
            for n in range(j):
                    dp[i][j] += dp[i][n]
    return dp[raw-1][col-1]  # 最终状态


if __name__ == "__main__":
    r, c = 4, 4
    print(juedipickequipment(r, c))

```

***
