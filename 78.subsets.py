#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            new_subsets = subsets.copy()
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets = new_subsets
        return subsets
# @lc code=end

