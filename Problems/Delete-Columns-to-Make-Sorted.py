1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        res = 0
4
5        for col in zip(*strs):
6            if list(sorted(col)) != list(col):
7                res += 1
8
9        return res
10