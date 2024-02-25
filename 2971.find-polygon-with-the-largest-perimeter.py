#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        total = sum(nums[:2])
        perimeter = -1
        for i in range(2, len(nums)):
            if nums[i] < total:
                perimeter = total + nums[i]
            total  += nums[i]
        return perimeter
# @lc code=end

