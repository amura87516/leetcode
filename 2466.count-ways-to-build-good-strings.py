#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#

# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[zero] += 1
        dp[one] += 1

        
        for i in range(high+1):
            if i+one <= high:
                dp[i+one] = (dp[i+one]+dp[i]) % (10**9+7)
            if i+zero <= high:
                dp[i+zero] = (dp[i+zero]+dp[i]) % (10**9+7)
        
        res = 0
        for i in range(low, high+1):
            res = (res + dp[i]) % (10**9+7)
        return res
# @lc code=end

2\n3\n1\n2