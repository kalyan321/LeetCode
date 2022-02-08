class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            s = 0
            for i in num:
                s += int(i)
            num = str(s)
        return int(num)