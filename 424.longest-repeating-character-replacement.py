#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        cnt = {s[0]: 1} # element frequent in current slidding window
        while right < len(s):
            # find most frequent char in current sliding window
            most_frequent_char = s[left]
            for char in cnt:
                if cnt[char] > cnt[most_frequent_char]:
                    most_frequent_char = char

            # check if current status allow replace all non-most-frequent elemet
            if right - left + 1 <= cnt[most_frequent_char] + k:
                # update new result
                res = max(res, right - left + 1)

                # add new char to slidding window
                right += 1
                if right >= len(s):
                    break
                if s[right] in cnt:
                    cnt[s[right]] += 1
                else:
                    cnt[s[right]] = 1
            # invalid status, pop front element
            else:
                cnt[s[left]] -= 1
                left += 1

        return res
# @lc code=end

