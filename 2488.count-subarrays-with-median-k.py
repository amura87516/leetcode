#
# @lc app=leetcode id=2488 lang=python3
#
# [2488] Count Subarrays With Median K
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        index = nums.index(k)

        res = 1
        right_counter = {}
        for i in range(index+1, len(nums)):
            if nums[i] >= k:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = dp[i-1]-1

            if dp[i] in [0, 1]:
                res += 1

            if dp[i] in right_counter:
                right_counter[dp[i]] += 1
            else:
                right_counter[dp[i]] = 1

        for i in range(index-1, -1, -1):
            if nums[i] >= k:
                dp[i] = dp[i+1]+1
            else:
                dp[i] = dp[i+1]-1

            if dp[i] in [0, 1]:
                res += 1

            if -dp[i] in right_counter:
                res += right_counter[-dp[i]]
            if -dp[i]+1 in right_counter:
                res += right_counter[-dp[i]+1]

        return res
# @lc code=end

