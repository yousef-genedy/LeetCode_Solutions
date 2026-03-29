1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
4            return False
5
6        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
7            return False
8
9        return True
10