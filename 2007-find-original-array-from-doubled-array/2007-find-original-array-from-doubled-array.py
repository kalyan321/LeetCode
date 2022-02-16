from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        org = []
        d = defaultdict(int)
        for i in changed:
            d[i] += 1
        for i in changed:
            if d[i] > 0:
                d[i] -= 1
                if d[2*i] == 0:
                    return []
                else:
                    org.append(i)
                    d[2*i] -= 1
                # d[i] -= 1
                # d[2*i] -= 1
        return org if len(org) == math.ceil(len(changed)/2) else []
                