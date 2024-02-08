#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:                
        dp = [i for i in range(n+1)]
        for i in range(1, math.floor(math.sqrt(n))+1):
            dp[i**2] = 1
        for i in range(1, n+1):
            for j in range(1, math.floor(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i - j**2] + dp[j**2])
        return dp[n]
# @lc code=end

