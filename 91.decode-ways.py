#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp[0] = 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            # can append to previous result 
            if s[i] != "0":
                dp[i] = dp[i-1]
            
            # can merge with previous result 
            if s[i-1: i+1] <= "26" and s[i-1] != "0":
                dp[i] += dp[i-2] if i >= 2 else 1
                
        return dp[-1]
# @lc code=end
"2101"