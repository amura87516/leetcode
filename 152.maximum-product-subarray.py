#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # res = -2e5

        # candidates = []
        # candidate = []
        # for num in nums:
        #     res = max(res, num)
        #     if num == 1:
        #         continue
        #     elif num == 0:
        #         candidates.append(candidate)
        #         candidate = []
        #     else:
        #         candidate.append(num)
        # if len(candidate) > 0:
        #     candidates.append(candidate)

        # for candidate in candidates:
        #     for i in range(len(candidate)):
        #         temp = candidate[i]
        #         res = max(res, temp)
        #         for j in range(i+1, len(candidate)):
        #             temp *= candidate[j]
        #             res = max(res, temp)
        # return res
        
        res = nums[0]
        status = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            new_status = [None, None]
            if nums[i] < 0:
                new_status[0] = max(nums[i], status[1] * nums[i])
                new_status[1] = min(nums[i], status[0] * nums[i])
            else:
                new_status[0] = max(nums[i], status[0] * nums[i])
                new_status[1] = min(nums[i], status[1] * nums[i])

            
            status = new_status
            res = max(res, status[0])
            # print(status)

        return res

        
# @lc code=end

