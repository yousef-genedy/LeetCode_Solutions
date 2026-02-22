1class Solution:
2    def binaryGap(self, n: int) -> int:
3        s = bin(n)[2:]
4        res = 0
5        prev = -1
6
7        for i, ch in enumerate(s):
8            if ch == '1':
9                if prev != -1:
10                    res = max(res, i - prev)
11                prev = i
12
13        return res
14