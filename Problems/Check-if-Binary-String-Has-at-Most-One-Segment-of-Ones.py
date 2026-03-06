1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        found = False
4
5        for i in range(len(s)):
6            if i > 0 and s[i] == '0' and s[i - 1] == '1':
7                found = True
8            
9            if found and s[i] == '1':
10                return False
11
12        return True
13