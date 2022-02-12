from collections import defaultdict, Counter
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d = defaultdict(list)
        for i in range(len(pattern)):
            d[pattern[i]].append(i)
        res = []
        for word in words:
            for lst in d:
                s = set()
                for ind in d[lst]:
                    # print(ind)
                    s.add(word[ind])
                if len(s) != 1:
                    print(s)
                    break
            else:
                if len(d) == len(Counter(word)):
                    res.append(word)
        return res