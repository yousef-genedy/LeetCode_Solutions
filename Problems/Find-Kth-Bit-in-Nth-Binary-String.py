1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        def invert(x: str) -> str:
4            return ''.join('1' if c == '0' else '0' for c in x)
5
6        s = "0"
7        for i in range(2, n + 1):
8            s = s + "1" + invert(s)[::-1]
9
10        return s[k - 1]
11