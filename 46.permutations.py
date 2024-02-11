#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums.copy()

        # search peak from back
        peak_index = len(nums)-1
        while peak_index > 0 and nums[peak_index-1] >= nums[peak_index]:
            peak_index -= 1

        if peak_index == 0:
            nums.sort() 
        else:
            # sort RHS
            temp = nums[peak_index:]
            temp.sort()
            nums[peak_index:] = temp

            # pick least number that is greater than nums[peak-1]
            for index in range(peak_index, len(nums)):
                if nums[index] > nums[peak_index-1]:
                    nums[peak_index-1], nums[index] = nums[index], nums[peak_index-1]
                    break
        return nums

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [nums]
        next_permutation = self.nextPermutation(nums)
        while next_permutation != nums:
            res.append(next_permutation)
            next_permutation = self.nextPermutation(next_permutation)
        return res
# @lc code=end

