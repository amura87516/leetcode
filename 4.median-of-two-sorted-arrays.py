#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        median_index = (len(nums1) + len(nums2)+1) / 2
        p1 = 0
        p2 = 0
        while p1+p2 < median_index and p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        while p1+p2 < median_index and p1 < len(nums1):
            merged.append(nums1[p1])
            p1 += 1

        while p1+p2 < median_index and p2 < len(nums2):
            merged.append(nums2[p2])
            p2 += 1

        if p1+p2 == median_index:
            return merged[-1]
        else:
            return (merged[-1]+merged[-2])/2
# @lc code=end

[1,2]\n[3,4]