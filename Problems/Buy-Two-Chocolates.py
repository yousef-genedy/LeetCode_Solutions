1class Solution:
2    def buyChoco(self, prices: List[int], money: int) -> int:
3        min1 = math.inf
4        min2 = math.inf
5
6        for p in prices:
7            if p <= min1:
8                min2 = min1
9                min1 = p
10            elif p < min2:
11                min2 = p
12
13        min_cost = min1 + min2
14        return money - min_cost if money >= min_cost else money
15