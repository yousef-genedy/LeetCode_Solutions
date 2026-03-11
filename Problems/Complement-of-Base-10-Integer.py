1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        return int("".join("1" if c == "0" else "0" for c in bin(n)[2:]), 2)
4