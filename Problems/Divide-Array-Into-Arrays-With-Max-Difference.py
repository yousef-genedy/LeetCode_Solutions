1class Solution:
2    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5
6        for i in range(0, n, 3):
7            if nums[i + 2] - nums[i] > k:
8                return []
9
10        return [nums[i : i + 3] for i in range(0, n, 3)]