1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        pos = defaultdict(list)
4
5        for i, x in enumerate(nums):
6            pos[x].append(i)
7
8        res = float('inf')
9
10        for idxs in pos.values():
11            if len(idxs) >= 3:
12                for i in range(len(idxs) - 2):
13                    res = min(res, 2 * (idxs[i + 2] - idxs[i]))
14
15        return -1 if res == float('inf') else res
16