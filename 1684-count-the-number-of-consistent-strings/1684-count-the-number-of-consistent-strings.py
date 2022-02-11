class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = collections.Counter(allowed)
        count = 0
        for word in words:
            for i in word:
                if i not in c:
                    break
            else:
                count += 1
        return count