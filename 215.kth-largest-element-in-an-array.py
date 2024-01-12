#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def quick_sort(self, nums: List[int], left: int, right: int):
        pivot = right
        prev_larger_index = left
        for index in range(left, right):
            if nums[index] > nums[pivot]:
                nums[prev_larger_index], nums[index] = nums[index], nums[prev_larger_index]
                prev_larger_index += 1

        nums[prev_larger_index], nums[pivot] = nums[pivot], nums[prev_larger_index]

        # print(nums[left:right+1], prev_larger_index)
        return nums, prev_larger_index

    def recursive(self, nums: List[int], k: int, left: int, right: int):
        nums, pivot = self.quick_sort(nums, left, right)
        # print(nums, nums[left:right+1], pivot-left, k)
        if pivot == k - 1:
            return nums[pivot]
        elif pivot > k - 1:
            return self.recursive(nums, k, left, pivot-1)
        else:
            return self.recursive(nums, k, pivot+1, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.recursive(nums, k, 0, len(nums)-1)
# @lc code=end
[6, 5, 4]\n2
[3,2,1,5,6,4]\n2
[3,2,3,1,2,4,5,5,6]\n4
[2,1]\n2
[5, 5, 3]\n3