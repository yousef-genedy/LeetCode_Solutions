1class Solution:
2    def frequencySort(self, s: str) -> str:
3        count = dict(sorted(Counter(s).items(), key=lambda item: item[1], reverse=True))
4        
5        ans = ""
6        for k, v in count.items():
7            ans += k * v
8
9        return ans
10