1class Solution:
2    def arraySign(self, nums: List[int]) -> int:
3        neg = 0
4
5        for n in nums:
6            if n == 0:
7                return 0
8            if n < 0:
9                neg += 1
10
11        return 1 if neg % 2 == 0 else -1
12