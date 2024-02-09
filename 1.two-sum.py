#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        position = {}
        for i in range(len(nums)):
            if target - nums[i] in position:
                return (position[target - nums[i]], i)
            position[nums[i]] = i
# @lc code=end
[0,4,3,0]\n0