#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#

# @lc code=start
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        prev = nums[-1]
        for i in range(2, len(nums)+1):
            cur = nums[-i]
            if cur < prev:
                prev = cur
            if cur > prev:
                cnt = ceil(cur / prev)
                res = res + cnt - 1

                shortage = cnt * prev - cur
                prev = prev - ceil(shortage / cnt)

        return res
# @lc code=end
