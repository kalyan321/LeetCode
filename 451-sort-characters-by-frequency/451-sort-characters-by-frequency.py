from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = list(Counter(s).items())
        c.sort(key = lambda x : x[1])
        s = ""
        for key, val in c:
            s = key * val + s
        return s
        