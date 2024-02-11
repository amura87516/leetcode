#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                # pivot in right
                if nums[mid] <= target and target <= nums[right]:
                    # target in right
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # pivot in right
                if nums[left] <= target and target <= nums[mid]:
                    # target in left
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
# @lc code=end

https://www.cnblogs.com/grandyang/p/4325648.html