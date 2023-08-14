#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution 1
        # O(nlogk)
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > k:
                heappop(pq)
        return pq[0]

        # solution 2
        # O(nlogn)
        # nums.sort()
        # return nums[-k]
        
# @lc code=end

