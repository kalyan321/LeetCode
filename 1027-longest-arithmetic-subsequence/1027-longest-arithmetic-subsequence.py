class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        res = 2
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff = nums[j] - nums[i]
                if diff in dp:
                    if i in dp[diff]:
                        dp[diff][j] = dp[diff][i] + 1
                    else:
                        dp[diff][j] = 2
                else:
                    dp[diff] = {}
                    dp[diff][j] = 2
                res = max(res, dp[diff][j])
        return res