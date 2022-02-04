class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        summ = satisfaction[0]
        for i in range(1, len(satisfaction)):
            curr = satisfaction[i]
            satisfaction[i] += satisfaction[i-1] + summ
            summ += curr
        return 0 if max(satisfaction) < 0 else max(satisfaction) 