#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = [int(math.pow(2, 31)-1)] * len(nums)
        minimum = nums[0]
        for i in range(1, len(nums)):
            left[i] = minimum
            minimum = min(minimum, nums[i])
            
        right = [-int(math.pow(2, 31))] * len(nums)
        maximum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = maximum
            maximum = max(maximum, nums[i])

        for i in range(len(nums)):
            if left[i] < nums[i] and nums[i] < right[i]:
                return True
        return False

# @lc code=end

