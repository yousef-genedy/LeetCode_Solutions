1class Solution:
2    def findFinalValue(self, nums: List[int], original: int) -> int:
3        s = set(nums)
4
5        while original in s:
6            original *= 2
7
8        return original
9