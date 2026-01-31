1class Solution:
2    def minOperations(self, nums: List[int], x: int) -> int:
3        s = sum(nums)
4        target = s - x
5
6        if target < 0:
7            return -1
8        
9        curr = l = 0
10        mx_len = -1
11
12        for r in range(len(nums)):
13            curr += nums[r]
14
15            while curr > target:
16                curr -= nums[l]
17                l += 1
18            
19            if curr == target:
20                mx_len = max(mx_len, r - l + 1)
21
22        return -1 if mx_len == -1 else len(nums) - mx_len
23