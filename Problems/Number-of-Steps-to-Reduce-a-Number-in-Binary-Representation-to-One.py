1class Solution:
2    def numSteps(self, s: str) -> int:
3        count = 0
4
5        n = int(s, 2)
6
7        while n != 1:
8            if n & 1:
9                n += 1
10            else:
11                n //= 2
12
13            count += 1
14
15        return count
16