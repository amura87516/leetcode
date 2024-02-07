#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        if nums[0] >= 0:
            dp[0] = [nums[0], 0]
        else:
            dp[0] = [0, nums[0]]

        maxinum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i][0] = max(nums[i], nums[i] * dp[i-1][0])
                dp[i][1] = min(0, nums[i] * dp[i-1][1])
            else:
                dp[i][0] = max(0, nums[i] * dp[i-1][1])
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
            maxinum = max(maxinum, dp[i][0], dp[i][0])

        return maxinum
# @lc code=end
[-2]
