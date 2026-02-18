1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        n = bin(n)[2:]
4
5        for a, b in pairwise(n):
6            if a == b:
7                return False
8
9        return True
10