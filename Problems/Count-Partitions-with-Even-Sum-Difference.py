1class Solution:
2    def countPartitions(self, nums: List[int]) -> int:
3        return 0 if sum(nums) & 1 else len(nums) - 1
4