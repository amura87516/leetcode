#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=left
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)

        left = 0
        s = set()
        maxinum = 0
        for right in range(len(nums)):
            while nums[right] in s:
                s.remove(nums[left])
                left += 1

            s.add(nums[right])

            if right - left + 1== k:
                maxinum = max(maxinum, pre_sum[right+1] - pre_sum[left])
                s.remove(nums[left])
                left += 1
        
        return maxinum
# @lc code=right
