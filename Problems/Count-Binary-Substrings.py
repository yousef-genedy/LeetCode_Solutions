1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        res = prev = 0
4        curr = 1
5
6        for i in range(1, len(s)):
7            if s[i] == s[i - 1]:
8                curr += 1
9            else:
10                res += min(prev, curr)
11                prev = curr
12                curr = 1
13
14        res += min(prev, curr)
15
16        return res
17