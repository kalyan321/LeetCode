class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        summ = len(prices)
        count = 0
        for i in range(1, len(prices)):
            if (prices[i-1] - prices[i]) == 1:
                count += 1
            elif count > 0:
                summ += (count*(count + 1))//2
                count = 0
        if count > 0:
            summ += (count*(count + 1))//2
        return summ