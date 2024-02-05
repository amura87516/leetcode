#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                p += 1
            nums[p] = nums[i]
        return p + 1
# @lc code=end

