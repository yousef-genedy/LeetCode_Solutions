1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        return [
4            f"{h}:{m:02d}"
5            for h in range(12)
6            for m in range(60)
7            if h.bit_count() + m.bit_count() == turnedOn
8        ]
9