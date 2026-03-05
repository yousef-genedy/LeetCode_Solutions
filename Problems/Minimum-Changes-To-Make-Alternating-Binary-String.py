1class Solution:
2    def minOperations(self, s: str) -> int:
3        alt1 = alt2 = 0
4
5        for i, c in enumerate(s):
6            if c != ("0" if i % 2 == 0 else "1"):
7                alt1 += 1
8
9            if c != ("1" if i % 2 == 0 else "0"):
10                alt2 += 1
11
12        return min(alt1, alt2)
13