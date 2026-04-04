1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        l = 0
4        res = 0
5
6        for r in range(len(prices)):
7            if r > 0 and prices[r - 1] - prices[r] != 1:
8                l = r
9
10            res += (r - l + 1)
11
12        return res
13