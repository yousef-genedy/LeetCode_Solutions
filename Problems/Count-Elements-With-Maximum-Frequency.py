1class Solution:
2    def maxFrequencyElements(self, nums: List[int]) -> int:
3        count = Counter(nums)
4
5        mx_freq = max(count.values())
6
7        res = 0
8        for n in nums:
9            if count[n] == mx_freq:
10                res += 1
11
12        return res
13