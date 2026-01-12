1class Solution:
2    def isPowerOfThree(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        
6        while n % 3 == 0:
7            n //= 3
8
9        return n == 1
10