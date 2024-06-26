#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in range(len(nums)):
            subsets += [subset + [nums[i]] for subset in subsets]
        return subsets
# @lc code=end