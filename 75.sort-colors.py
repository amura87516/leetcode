#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = []
        for num in nums:
            heappush(q, num)

        index = 0
        while len(q) > 0:
            nums[index] = heappop(q)
            index += 1
# @lc code=end

