1class Solution:
2    def removeStars(self, s: str) -> str:
3        st = []
4
5        for c in s:
6            if c == '*':
7                st.pop()
8            else:
9                st.append(c)
10
11        return ''.join(st)
12