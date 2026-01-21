1class Solution:
2    def frequencySort(self, s: str) -> str:
3        count = Counter(s)
4        bucket = defaultdict(list)
5
6        for k, v in count.items():
7            bucket[v].append(k)
8
9        res = []
10        for i in range(len(s), 0, -1):
11            for c in bucket[i]:
12                res.append(c * i)
13
14        return ''.join(res)
15