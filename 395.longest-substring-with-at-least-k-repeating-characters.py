#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for left in range(len(s)):
            counter = [0] * 26
            for right in range(left, len(s)):
                counter[ord(s[right]) - ord('a')] += 1

                valid = True
                for cnt in counter:
                    if cnt > 0 and cnt < k:
                        valid = False
                        break
                if valid:
                    res = max(res, right - left + 1)
        return res
# @lc code=end

"ababbc"\n2