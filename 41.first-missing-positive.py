#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        expected_nums = [False for i in range(len(nums))]
        for num in nums:
            if num > 0 and num-1 < len(expected_nums):
                expected_nums[num-1] = True
        
        for i in range(len(nums)):
            if not expected_nums[i]:
                return i+1
        return len(nums)+1
# @lc code=end
[1]

