1class Solution:
2    def concatenatedBinary(self, n: int) -> int:
3        res = []
4
5        for i in range(n + 1):
6            res.append(bin(i)[2:])
7
8        return int(''.join(res), 2) % (10 ** 9 + 7)
9