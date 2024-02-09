#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def binary_search_insert_position(self, arr, target):
        # O(log(n))
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return right

    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(nlog(n))
        dp = [nums[0]]
        for i in range(1, len(nums)):
            pos = self.binary_search_insert_position(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
        return len(dp)
# @lc code=end

[0,1,0,3,2,3]
[7,7,7,7,7,7,7]