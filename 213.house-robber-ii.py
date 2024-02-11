#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def rob_normal(nums, left, right):
            dp = nums.copy()
            dp[left+1] = max(dp[left], dp[left+1])
            for index in range(left+2, right+1):
                dp[index] = max(dp[index-2]+nums[index], dp[index-1])
            return dp[right]
        
        return max(rob_normal(nums, 0, len(nums)-2), rob_normal(nums, 1, len(nums)-1))
    
# @lc code=end
[1,1,1,2]
[200,3,140,20,10]
[1,3,1,3,100]
[1,2,3,1]
[4,1,2,7,5,3,1]
[2,7,7,7,4]