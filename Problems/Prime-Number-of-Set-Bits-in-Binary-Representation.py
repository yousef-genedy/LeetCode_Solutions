1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        def is_prime(n: int) -> bool:
4            if n <= 1:
5                return False
6            
7            for i in range(2, n):
8                if n % i == 0:
9                    return False
10
11            return True
12
13        count = 0
14        for n in range(left, right + 1):
15            if is_prime(n.bit_count()):
16                count += 1
17
18        return count
19