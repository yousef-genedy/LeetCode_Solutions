1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        nums.sort()
4        l, r = 0, len(nums) - 1
5        max_sum = 0
6
7        while l < r:
8            curr = nums[l] + nums[r]
9            max_sum = max(max_sum, curr)
10
11            l += 1
12            r -= 1
13
14        return max_sum
15