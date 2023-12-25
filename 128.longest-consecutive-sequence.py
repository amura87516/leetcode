#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()

        combo = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] + 1 == nums[i]:
                combo += 1
                res = max(res, combo)
            else:
                combo = 1
        return res
# @lc code=end

