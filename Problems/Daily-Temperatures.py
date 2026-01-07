1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        ans = [0] * len(temperatures)
4        stack = []
5
6        for i, temp in enumerate(temperatures):
7            while stack and temp > temperatures[stack[-1]]:
8                prev_idx = stack.pop()
9                ans[prev_idx] = i - prev_idx
10            stack.append(i)
11
12        return ans
13