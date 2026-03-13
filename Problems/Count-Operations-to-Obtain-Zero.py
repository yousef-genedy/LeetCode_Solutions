1class Solution:
2    def countOperations(self, num1: int, num2: int) -> int:
3        res = 0
4        while num1 != 0 and num2 != 0:
5            if num1 >= num2:
6                num1 -= num2
7            else:
8                num2 -= num1
9            res += 1
10
11        return res
12