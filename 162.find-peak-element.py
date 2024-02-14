#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left) + left
            if (mid == 0 or nums[mid-1] <= nums[mid]) and (mid == len(nums)-1 or nums[mid] >= nums[mid+1]):
                return mid
            elif (mid == 0 or nums[mid-1] <= nums[mid]) and (mid == len(nums)-1 or nums[mid] <= nums[mid+1]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
# @lc code=end