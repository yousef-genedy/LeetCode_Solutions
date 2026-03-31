1class Solution:
2    def buyChoco(self, prices: List[int], money: int) -> int:
3        prices.sort()
4
5        min1 = math.inf
6        min2 = math.inf
7
8        for p in prices:
9            if p <= min1:
10                min2 = min1
11                min1 = p
12            elif p < min2:
13                min2 = p
14
15        min_cost = min1 + min2
16        return money - min_cost if money >= min_cost else money
17