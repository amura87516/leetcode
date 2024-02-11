#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return max(nums)

        dp = nums.copy()
        dp[1] = max(dp[0], dp[1])
        for index in range(2, len(nums)):
            dp[index] = max(dp[index-2]+nums[index], dp[index-1])
        return dp[-1]
# @lc code=end

