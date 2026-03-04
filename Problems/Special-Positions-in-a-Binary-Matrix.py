1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        r, c = len(mat), len(mat[0])
4        row_cnt, col_cnt = [0] * r, [0] * c
5
6        for i, row in enumerate(mat):
7            row_cnt[i] = sum(row)
8
9        for j, col in enumerate(zip(*mat)):
10            col_cnt[j] = sum(col)
11        
12        res = 0
13        for i in range(r):
14            for j in range(c):
15                if mat[i][j] == 1 and row_cnt[i] == 1 and col_cnt[j] == 1: 
16                    res += 1
17
18        return res
19