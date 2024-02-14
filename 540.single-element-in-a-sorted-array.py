#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left)//2 + left
            if (mid == 0 or nums[mid-1] != nums[mid]) and (mid == len(nums)-1 or nums[mid] != nums[mid+1]):
                # different with both left and right elements. target found
                return nums[mid]
            elif (mid == 0 or nums[mid-1] == nums[mid]) and (mid & 1 == 1) or \
                (mid == len(nums)-1 or nums[mid] == nums[mid+1]) and (mid & 1 == 0):
                # same as left element and mid is odd, or same as right element and mid is even
                left = mid + 1
            else:
                right = mid - 1
        return -1
# @lc code=end

