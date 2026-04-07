1class Solution:
2    def maximumOddBinaryNumber(self, s: str) -> str:
3        ones = s.count('1')
4        zeros = len(s) - ones
5
6        return '1' * (ones - 1) + '0' * zeros + '1'
7