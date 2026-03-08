1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        n = len(nums)
4        bin_set = set(nums)
5
6        for i in range(2 ** n):
7            b = bin(i)[2:].zfill(n)
8            if b not in bin_set:
9                return b
10