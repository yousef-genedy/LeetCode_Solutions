1class Solution:
2    def bestClosingTime(self, customers: str) -> int:
3        binary_str = customers.replace('Y', '0').replace('N', '1')
4        visit = int(binary_str, 2)
5
6        n = len(customers)
7        state = int('1' * n, 2)
8
9        idx, op = 0, float('inf')
10
11        for i in range(n + 1):
12            curr = visit ^ state
13            state >>= 1
14
15            cnt = curr.bit_count()
16            if cnt < op:
17                idx = i
18                op = cnt
19
20        return idx
21