#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_roduct = 1
        zero_cnt = 0
        zero_index = None
        for index, num in enumerate(nums):
            if num is 0:
                if zero_index is not None:
                    return [0] * len(nums)
                else:
                    zero_index = index
            else:
                total_roduct *= num

        if zero_index is not None:
            res = [0] * len(nums)
            res[zero_index] = total_roduct
            return res
        else:
            res = []
            for num in nums:
                res.append(total_roduct // num)
            return res

# @lc code=end

