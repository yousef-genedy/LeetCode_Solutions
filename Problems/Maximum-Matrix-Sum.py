1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        res = 0
4        neg_count = 0
5        min_abs_neg = float('inf')
6
7        for row in matrix:
8            for e in row:
9                num = abs(e)
10                res += num
11                min_abs_neg = min(min_abs_neg, num)
12
13                if e <= 0:
14                    neg_count += 1
15                    
16        return res if neg_count % 2 == 0 else res - 2 * min_abs_neg
17