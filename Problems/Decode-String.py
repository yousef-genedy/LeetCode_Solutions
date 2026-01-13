1class Solution:
2    def decodeString(self, s: str) -> str:
3        st = []
4        curr = ""
5        k = 0
6
7        for c in s:
8            if c.isdigit():
9                k = k * 10 + int(c)
10            elif c == '[':
11                st.append((curr, k))
12                curr, k = "", 0
13            elif c.isalpha():
14                curr += c
15            elif c == ']':
16                prev, cnt = st.pop()
17                curr = prev + curr * cnt
18            
19        return curr
20