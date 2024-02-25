#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        divisibles= [1 if num % p == 0 else 0 for num in nums]
        pre_sum = [0]
        for cnt in divisibles:
            pre_sum.append(pre_sum[-1]+cnt)

        cnt = 0
        existed_ans = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                divisible_cnt = pre_sum[j+1] - pre_sum[i]
                if divisible_cnt <= k and tuple(nums[i:j+1]) not in existed_ans:
                    existed_ans[tuple(nums[i:j+1])] = True
                    cnt += 1
        return cnt
# @lc code=end

