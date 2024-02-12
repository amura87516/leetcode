#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != candidate:
                cnt -= 1
                if cnt == -1:
                    candidate = nums[i]
                    cnt = 1
            else:
                cnt += 1
        return candidate       
# @lc code=end