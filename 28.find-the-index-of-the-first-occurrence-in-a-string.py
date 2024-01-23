#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, s: str, target: str) -> int:
        # dp[i] = same prefix index 
        dp = [-1] * len(target)
        p1 = 0
        p2 = 1
        while p2 < len(target):
            if target[p1] == target[p2]:
                dp[p2] = p1
                p1 += 1
                p2 += 1
            else:
                if p1 == 0:
                    p2 += 1
                else:
                    p1 = dp[p1-1] + 1

        p1 = 0
        p2 = 0
        while p1 < len(target) and p2 < len(s):
            if target[p1] == s[p2]:
                p1 += 1
                p2 += 1
            else:
                if p1 == 0:
                    p2 += 1
                else:
                    p1 = dp[p1-1] + 1

        if p1 == len(target):
            return p2 - len(target)
        else:   
            return -1
# @lc code=end
