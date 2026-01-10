1class Solution:
2    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
3        st = []
4        i = 0
5
6        for x in pushed:
7            st.append(x)  
8            while st and st[-1] == popped[i]:
9                st.pop()
10                i += 1
11
12        return len(st) == 0
13