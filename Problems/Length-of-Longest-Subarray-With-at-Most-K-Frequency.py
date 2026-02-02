1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        freq = defaultdict(int)
4        l = res = 0
5
6        for r in range(len(nums)):
7            freq[nums[r]] += 1
8
9            while freq[nums[r]] > k:
10                freq[nums[l]] -= 1
11                l += 1
12
13            res = max(res, r - l + 1)
14
15        return res
16