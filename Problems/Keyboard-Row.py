1class Solution:
2    def findWords(self, words: List[str]) -> List[str]:
3        res = []
4        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
5
6        for word in words:
7            w = set(word.lower())
8            if any(w.issubset(row) for row in rows):
9                res.append(word)
10
11        return res
12