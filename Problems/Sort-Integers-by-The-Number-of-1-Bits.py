1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        return sorted(arr, key=lambda x: (x.bit_count(), x))
4