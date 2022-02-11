class Solution:
    def sortSentence(self, s: str) -> str:
        l = ['']*9
        s = s.split()
        for i in s:
            # pos = i[len(i)]
            l[int(i[len(i) - 1]) - 1] = i[0:-1]
        return " ".join(l).strip()