#
# @lc app=leetcode id=2369 lang=python3
#
# [2369] Check if There is a Valid Partition For The Array
#

# @lc code=start
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        combo2 = [False for i in range(len(nums))]
        combo3 = [False for i in range(len(nums))]
        consecutive2 = [False for i in range(len(nums))]
        consecutive3 = [False for i in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                combo2[i] = True
            if nums[i-1] == nums[i] - 1:
                consecutive2[i] = True

        for i in range(2, len(nums)):
            if combo2[i-1] and nums[i-1] == nums[i]:
                combo3[i] = True
            if consecutive2[i-1] and nums[i-1] == nums[i] - 1:
                consecutive3[i] = True

        res = [False for i in range(len(nums))]
        res[1] = combo2[1]
        if len(nums) > 2:
            res[2] = combo3[2] or consecutive3[2]

        for i in range(3, len(nums)):
            res[i] =  res[i-2] and combo2[i] or res[i-3] and combo3[i] or res[i-3] and consecutive3[i]
        
        return res[-1]

        

# @lc code=end

