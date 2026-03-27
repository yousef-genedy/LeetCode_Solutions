1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        
4        def shift_left(arr):
5            sv = arr[0]
6            for i in range(len(arr) - 1):
7                arr[i] = arr[i + 1]
8
9            arr[-1] = sv
10
11            return arr
12
13        def shift_right(arr):
14            sv = arr[-1]
15            for i in range(len(arr) - 1, 0, -1):
16                arr[i] = arr[i - 1]
17
18            arr[0] = sv
19
20            return arr
21
22        copy = [row[:] for row in mat]
23        k %= len(mat[0])
24
25        while k > 0:
26            for i in range(len(mat)):
27                if i & 1:
28                    mat[i] = shift_right(mat[i])
29                else:
30                    mat[i] = shift_left(mat[i])
31
32            k -= 1
33
34        for i in range(len(mat)):
35            for j in range(len(mat[0])):
36                if copy[i][j] != mat[i][j]:
37                    return False
38
39        return True
40