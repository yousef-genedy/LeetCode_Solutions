1class Solution:
2    def smallestNumber(self, n: int) -> int:
3        return (1 << n.bit_length()) - 1
4