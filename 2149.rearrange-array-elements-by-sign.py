#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [num for num in nums if num >= 0]
        negatives = [num for num in nums if num < 0]
        res = []
        while len(res) < len(nums):
            if len(res) & 1 == 0:
                res.append(positives[len(res)//2])
            else:
                res.append(negatives[len(res)//2])
        return res
# @lc code=end