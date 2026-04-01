1class Solution:
2    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
3        cnt = 0
4
5        for i in range(len(arr1)):
6            valid = True
7
8            for j in range(len(arr2)):
9                if abs(arr1[i] - arr2[j]) <= d:
10                    valid = False
11                    break
12 
13            if valid:
14                cnt += 1
15
16        return cnt
17