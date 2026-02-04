1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        
4        def count(num):
5            c = 0
6            while num:
7                num //= 10
8                c += 1
9
10            return c
11
12        res = 0
13        for n in nums:
14            if count(n) % 2 == 0:
15                res += 1
16
17        return res
18