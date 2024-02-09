#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int, start: int) -> List[int]:
        # O(n)
        res = []
        position = {}
        for i in range(start, len(nums)):
            if target - nums[i] in position:
                res.append([position[target - nums[i]], i])
            position[nums[i]] = i
        return res
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for subres in self.twoSum(nums, target - nums[i] - nums[j], j+1):
                    subres = subres + [i, j]
                    subres = [nums[index] for index in subres]
                    subres.sort()
                    res.add(tuple(subres)) 
        return res
# @lc code=end

[-3,-2,-1,0,0,1,2,3]\n0
[-5,5,4,-3,0,0,4,-2]\n4