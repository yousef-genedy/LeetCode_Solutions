1class Solution:
2    def findLucky(self, arr: List[int]) -> int:
3        count = Counter(arr)
4
5        res = float('-inf')
6        for k, v in count.items():
7            if k == v:
8                res = max(res, k)
9
10        return -1 if res == float('-inf') else res
11