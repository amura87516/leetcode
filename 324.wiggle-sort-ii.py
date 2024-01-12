#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def reindex(self, index: int, n: int):
        return (2*index+1) % (n|1)
    def quick_select(self, nums: List[int], k: int, start: int, end: int):
        pivot = start
        p = start
        for index in range(start+1, end):
            if nums[index] <= nums[pivot]:
                p += 1
                nums[index], nums[p] = nums[p], nums[index]

        nums[pivot], nums[p] = nums[p], nums[pivot]

        return nums, p

    def quick_select_recursive(self, nums: List[int], kth: int, start: int, end: int):
        nums, pivot = self.quick_select(nums, kth, start, end)
        if kth == pivot:
            return pivot
        elif kth < pivot:
            return self.quick_select_recursive(nums, kth, start, pivot)
        else:
            return self.quick_select_recursive(nums, kth, pivot+1, end)
    
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        median_index = self.quick_select_recursive(nums, (len(nums))//2, 0, len(nums))

        mid = nums[median_index]
        left = 0
        right = len(nums) - 1
        cur = 0
        n = len(nums)
        while cur <= right:
            # if current value larger than mid, put it to head
            if nums[self.reindex(cur, n)] > mid:
                nums[self.reindex(left, n)], nums[self.reindex(cur, n)] = nums[self.reindex(cur, n)], nums[self.reindex(left, n)]
                left += 1
                cur += 1
            # if current value smaller than mid, put it to tail
            elif nums[self.reindex(cur, n)] < mid:
                nums[self.reindex(cur, n)], nums[self.reindex(right, n)] = nums[self.reindex(right, n)], nums[self.reindex(cur, n)]
                right -= 1
            # if current value equal to mid, do nothing
            else:
                cur += 1
# @lc code=end

[1,3,2,2,1,3]
[1]