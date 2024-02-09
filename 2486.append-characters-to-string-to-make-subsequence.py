#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for i in range(len(s)):
            if t[p] == s[i]:
                p += 1
                if p >= len(t):
                    break
        return len(t) - p
# @lc code=end

