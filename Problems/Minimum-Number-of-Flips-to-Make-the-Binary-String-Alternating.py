1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        double = 2 * s
5
6        alt1 = "".join(['1' if i % 2 == 0 else '0' for i in range(2 * n)])
7        alt2 = "".join(['0' if i % 2 == 0 else '1' for i in range(2 * n)])
8
9        diff1, diff2 = 0, 0
10        min_flips = len(double)
11
12        l = 0
13        for r in range(2 * n):
14            if double[r] != alt1[r]:
15                diff1 += 1
16            if double[r] != alt2[r]:
17                diff2 += 1
18
19            if (r - l + 1) > n:
20                if double[l] != alt1[l]:
21                    diff1 -= 1
22                if double[l] != alt2[l]:
23                    diff2 -= 1
24                l += 1
25
26            if (r - l + 1) == n:
27                min_flips = min(min_flips, diff1, diff2)
28
29        return min_flips
30