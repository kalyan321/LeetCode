class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        s1 = '10' * n
        s2 = '01' * n
        res = float('inf')
        ans1 = 0
        ans2 = 0
        for i in range(len(s)):
            if s[i] != s1[i]:
                ans1 += 1
            if s[i] != s2[i]:
                ans2 += 1
            if i >= n:
                if s[i-n] != s1[i-n]:
                    ans1 -=1
                if s[i-n] != s2[i-n]:
                    ans2 -= 1
            if i >= n - 1:
                res = min(res, ans1, ans2)
        return res