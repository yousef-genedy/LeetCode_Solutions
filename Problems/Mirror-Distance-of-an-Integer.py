1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        
4        def reverse(num: int) -> int:
5            res = 0
6
7            while num:
8                dig = num % 10
9                res = res * 10 + dig
10                num //= 10
11
12            return res
13    
14        return abs(n - reverse(n))