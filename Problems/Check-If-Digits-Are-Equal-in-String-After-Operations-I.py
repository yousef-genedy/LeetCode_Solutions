1class Solution:
2    def hasSameDigits(self, s: str) -> bool:
3        while len(s) > 2:
4            c = ""
5            for a, b in pairwise(s):
6                c += str((int(a) + int(b)) % 10)
7            s = c
8
9        return s[0] == s[1]
10