1class Solution:
2    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
3        arr.sort()
4
5        arr[0] = 1
6
7        for i in range(1, len(arr)):
8            arr[i] = min(arr[i], arr[i - 1] + 1)
9
10        return arr[-1]
11