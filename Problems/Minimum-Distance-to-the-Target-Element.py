1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        res = math.inf
4        n = len(nums)
5
6        for i in range(n):
7            if nums[i] == target:
8                res = min(res, abs(i - start))
9
10        for i in range(n - 1, -1, -1):
11            if nums[i] == target:
12                res = min(res, abs(i - start))
13
14        return res
15