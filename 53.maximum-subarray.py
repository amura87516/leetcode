#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        find  max (maximal after minimal) - manimal
        '''
        res = int(-1e4)
        total = 0
        minimal = 0
        for num in nums:
            total += num
            if minimal > total:
                minimal = total
                res = max(res, num)
            else:
                res = max(res, total - minimal)
        return res

# @lc code=end

