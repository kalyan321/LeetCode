class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.ans = 0
        def backtrack(pos,c,sco):
            if pos == len(words):
                self.ans = max(self.ans, sco)
                return
            backtrack(pos+1, c, sco)
            curr = collections.Counter(words[pos])
            if all(curr[k] <=c[k] for k in curr):
                s = 0
                for i in words[pos]:
                    # print(score, ord(i) - ord('a'))
                    s += score[ord(i) - ord('a')]
                backtrack(pos + 1, c - curr, sco + s)
        backtrack(0,collections.Counter(letters),0)
        return self.ans