#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_empty = [0]
        d = set([nums[0]])
        for i in range(1, len(nums)):
            if nums[i] in d:
                prev_empty.append(prev_empty[-1]+1)
            else:
                d.add(nums[i])
                prev_empty.append(prev_empty[-1])
        
        for i in range(len(nums)):
            nums[i - prev_empty[i]] = nums[i]

        return len(nums) - prev_empty[-1]
# @lc code=end

