#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n+1):
            if i+1 < n+1:
                dp[i+1] += dp[i]
            if i+2 < n+1:
                dp[i+2] += dp[i]
        return dp[-1]
# @lc code=end