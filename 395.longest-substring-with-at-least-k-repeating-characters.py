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
            cnt = [0] * 26
            for right in range(left, len(s)):
                cnt[ord(s[right]) - ord('a')] += 1

                valid = True
                for i in range(26):
                    if cnt[i] > 0 and cnt[i] < k:
                        valid = False
                        break
                if valid:
                    res = max(res, right - left + 1)
        return res



# @lc code=end

