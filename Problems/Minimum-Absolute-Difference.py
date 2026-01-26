1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        mn = float('inf')
4        arr.sort()
5
6        for a, b in pairwise(arr):
7            mn = min(mn, b - a)
8
9        return [[a, b] for a, b in pairwise(arr) if b - a == mn]
10