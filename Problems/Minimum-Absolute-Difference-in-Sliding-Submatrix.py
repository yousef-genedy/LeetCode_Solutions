1class Solution:
2    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        ans = []
5
6        for i in range(m - k + 1):
7            row = []
8            for j in range(n - k + 1):
9                vals = set()
10
11                for r in range(i, i + k):
12                    for c in range(j, j + k):
13                        vals.add(grid[r][c])
14                
15                vals = sorted(vals)
16                
17                if len(vals) <= 1:
18                    row.append(0)
19                else:
20                    best = float('inf')
21                    for x in range(1, len(vals)):
22                        best = min(best, vals[x] - vals[x - 1])
23                    row.append(best)
24
25            ans.append(row)
26
27        return ans
28