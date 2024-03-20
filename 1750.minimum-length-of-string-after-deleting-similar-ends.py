#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            target = s[0]
            left = 0
            right = len(s)-1
            while left + 1 < right and s[left+1] == target:
                left += 1
            while right - 1 > left and s[right-1] == target:
                right -= 1
            s = s[left+1:right]
            # print(s)
        return len(s)
# @lc code=end

