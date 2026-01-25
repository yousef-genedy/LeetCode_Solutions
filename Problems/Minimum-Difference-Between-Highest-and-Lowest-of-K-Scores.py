1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        nums.sort()
4
5        res = nums[-1]
6        for r in range(k - 1, len(nums)):
7            l = r - (k - 1)
8            res = min(res, nums[r] - nums[l])
9
10        return res
11