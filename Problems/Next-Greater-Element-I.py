1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        next_greater = {}
4        stack = []
5
6        for num in nums2:
7            while stack and stack[-1] < num:
8                next_greater[stack.pop()] = num
9            stack.append(num)
10
11        while stack:
12            next_greater[stack.pop()] = -1
13
14        res = []
15        for num in nums1:
16            res.append(next_greater[num])
17
18        return res
19