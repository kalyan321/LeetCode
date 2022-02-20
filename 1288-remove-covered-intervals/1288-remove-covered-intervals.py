class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        stack = []
        for i in intervals:
            if stack and  i[0] >= stack[-1][0] and i[1] <= stack[-1][1]:
                pass
            else:
                stack.append(i)
        return len(stack)