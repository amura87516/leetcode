#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = -1

        # O(n)
        for i in range(len(nums)):
            # when (val in range) and (val not in correct index) and (not duplicated val)
            while nums[i] > 0 and nums[i] < len(nums) and \
                nums[i] != i+1 and nums[nums[i]-1] != nums[i]:

                index1 = i
                index2 = nums[i]-1
                nums[index1], nums[index2] = nums[index2], nums[index1]

        # O(n)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1
# @lc code=end
[1]


[7,8,9,11,12]

[3,4,-1,1]
[-1,1,3,4]
[1,-1,3,4]