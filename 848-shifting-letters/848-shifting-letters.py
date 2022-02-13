class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        for i in range(len(shifts)-1, -1, -1):
            if i != len(shifts) - 1:
                shifts[i] += shifts[i+1]
            shifts [i] %= 26
            if shifts[i] == 0:
                shifts[i] = 26
        s = list(s)
        for i in range(len(s)):
            val = ord(s[i]) + shifts[i]
            if val > 122:
                val = val - 122 + 96
            s[i] = chr(val)
        return "".join(s)