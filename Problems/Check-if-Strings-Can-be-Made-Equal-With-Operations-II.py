1class Solution:
2    def checkStrings(self, s1: str, s2: str) -> bool:
3        even1 = [0] * 26
4        odd1 = [0] * 26
5        even2 = [0] * 26
6        odd2 = [0] * 26
7
8        for i in range(len(s1)):
9            idx1 = ord(s1[i]) - ord('a')
10            idx2 = ord(s2[i]) - ord('a')
11
12            if i % 2 == 0:
13                even1[idx1] += 1
14                even2[idx2] += 1
15            else:
16                odd1[idx1] += 1
17                odd2[idx2] += 1
18
19        return even1 == even2 and odd1 == odd2
20