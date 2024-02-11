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
        # search peak from back
        peak_index = len(nums)-1
        while peak_index > 0 and nums[peak_index-1] >= nums[peak_index]:
            peak_index -= 1

        if peak_index == 0:
            nums.sort() 
        else:
            # sort RHS
            temp = nums[peak_index:]
            temp.sort()
            nums[peak_index:] = temp

            # pick least number that is greater than nums[peak-1]
            for index in range(peak_index, len(nums)):
                if nums[index] > nums[peak_index-1]:
                    nums[peak_index-1], nums[index] = nums[index], nums[peak_index-1]
                    break
# @lc code=end
[1,1,5]
[1,1]
[2,3,1]
[4,2,4,4,3]
