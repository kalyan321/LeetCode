class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        for i in nums:
            if d[i+k] > 0:
                count += d[i+k]
            if d[i-k] > 0:
                count += d[i-k]
            d[i] += 1
        return count