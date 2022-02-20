class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        pos = 0
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[pos][0] and intervals[i][1] <= intervals[pos][1]:
                pass
            else:
                pos = i
                count += 1
        return count