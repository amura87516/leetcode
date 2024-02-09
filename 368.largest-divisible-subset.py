#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # O(nlogn)
        nums.sort()

        # O(n^2)
        dp = [[i] for i in range(len(nums))]
        longest = []
        for root in range(len(nums)-1, -1, -1):
            candidate = [nums[root]]
            for subnode in range(root+1, len(nums)):
                if nums[subnode] % nums[root] == 0 and len(candidate) < len(dp[subnode])+1:
                    candidate = [nums[root]] + dp[subnode]
            dp[root] = candidate

            if len(longest) < len(candidate):
                longest = candidate

        return longest 
# @lc code=end

