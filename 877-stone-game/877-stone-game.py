class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[[0,0] for i in range(len(piles))] for i in range(len(piles) + 1)]
        i = 0
        col_inc = 0
        row = len(piles)
        while i < row:
            j = col_inc
            while j < len(piles):
                
                if dp[i+1][j][1] + piles[i] < dp[i][j-1][1] + piles[j]:
                    dp[i][j][0] = dp[i][j-1][1] + piles[j]
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = dp[i+1][j][1] + piles[i]
                    dp[i][j][1] = dp[i][j-1][1]
                i += 1
                j += 1
            col_inc += 1
            row -= 1
        return dp[-1][-1][0] >= dp[-1][-1][1]