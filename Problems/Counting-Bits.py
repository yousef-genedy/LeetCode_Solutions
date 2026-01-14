1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4
5        for i in range(n + 1):
6            ans.append(i.bit_count())
7
8        return ans
9