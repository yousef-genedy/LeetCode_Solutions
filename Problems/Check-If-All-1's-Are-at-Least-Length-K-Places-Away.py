1class Solution:
2    def kLengthApart(self, nums: List[int], k: int) -> bool:
3        prev = -1
4
5        for i, b in enumerate(nums):
6            if b == 1:
7                if prev != -1 and i - prev <= k:
8                    return False
9                prev = i
10
11        return True