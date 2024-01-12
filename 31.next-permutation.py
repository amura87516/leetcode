#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find first_non_ascending_index
        first_non_ascending_index = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                first_non_ascending_index = i
                break
        
        # sort the ascending part
        nums[first_non_ascending_index+1:] = sorted(nums[first_non_ascending_index+1:])        
        
        # swap first_non_ascending_index and first element larger tham this element
        for i in range(first_non_ascending_index+1, len(nums)):
            if nums[i] > nums[first_non_ascending_index]:
                nums[first_non_ascending_index], nums[i] = nums[i], nums[first_non_ascending_index]
                break
# @lc code=end

