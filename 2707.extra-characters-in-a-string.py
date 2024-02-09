#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)

        dp = [i+1 for i in range(len(s))]
        for right in range(len(s)):
            for left in range(right+1):
                if s[left:right+1] in dictionary:
                    dp[right] = min(dp[right], dp[left-1] if left > 0 else 0)
                else:
                    dp[right] = min(dp[right], (dp[left-1] if left > 0 else 0) + right - left + 1)
        return dp[-1]
# @lc code=end

