1class Solution:
2    def smallestNumber(self, n: int) -> int:
3        c = len(bin(n)[2:])
4
5        return 2 ** c - 1
6
7