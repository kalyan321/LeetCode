class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        max_ending_here = 0
        for i in nums:
            max_ending_here = i + max(max_ending_here, 0)
            ans = max(ans, max_ending_here)
        right = [None] * len(nums)
        right[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + nums[i]
        max_right = [None] * n
        max_right[-1] = right[-1]
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1], right[i])
        summ = 0
        for i in range(n-2):
            summ += nums[i]
            ans = max(ans, summ + max_right[i+2])
        return ans