1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        n = len(mat[0])
4        k %= n
5
6        for i, row in enumerate(mat):
7            if i % 2 == 0:
8                shifted = row[k:] + row[:k]
9            else:
10                shifted = row[-k:] + row[:-k]
11
12            if row != shifted:
13                return False
14
15        return True
16