#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=left
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # O(n)
        cur_sum = 0
        pre_sum = [0]
        for num in nums:
            cur_sum += num
            pre_sum.append(cur_sum)

        prev_index = {nums[0]: 0} # previous visited index
        left = 0
        right = 0
        res = 0
        # O(n)
        while True:
            # if window size larger than limitation, pop front element
            while right - left + 1 > k:
                del prev_index[nums[left]]
                left += 1
                
            # expected window size, update result
            if right - left + 1 == k:
                res = max(res, pre_sum[right+1] - pre_sum[left])

            # get more new element
            right += 1
            if right >= len(nums):
                break

            # if the value of new element is visited before, pop all elements before that previous value
            if nums[right] in prev_index:
                for i in range(left, prev_index[nums[right]]):
                    del prev_index[nums[i]]
                left = prev_index[nums[right]] + 1
            
            # update previous visited index
            prev_index[nums[right]] = right

        return res
        
# @lc code=right

