#
# @lc app=leetcode id=2522 lang=python3
#
# [2522] Partition String Into Substrings With Values at Most K
#

# @lc code=start
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = 0
        max_window_length = len(str(k))
        index = 0
        while index < len(s):
            if int(s[index:index+max_window_length]) <= k:
                index += max_window_length
                res += 1
            elif max_window_length > 1:
                index += max_window_length - 1
                res += 1
            else:
                return -1
        return res
# @lc code=end

