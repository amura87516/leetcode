#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def binary_search(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left+right) // 2
            if nums[mid] == target:
                return target
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    new_res = self.binary_search(nums[k+1:], target - nums[i] - nums[j] - nums[k])
                    if new_res is not None:
                        res.add((nums[i], nums[j], nums[k], new_res))
        return list(res)

# @lc code=end

