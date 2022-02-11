class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = collections.Counter(s1)
        c1 = collections.Counter(s2[:len(s1)])
        k = len(s1)
        i = 0
        while k < len(s2):
            if len(c - c1) == 0:
                return True
            c1[s2[i]] -= 1
            c1[s2[k]] += 1
            i += 1
            k += 1
        return True if len(c - c1) == 0 else False