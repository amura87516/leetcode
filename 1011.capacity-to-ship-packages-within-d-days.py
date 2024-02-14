#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (right-left)//2 + left

            # count total days
            total_days = 0
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    cur = weight
                    total_days += 1
                else:
                    cur += weight
            total_days += 1


            if total_days <= days:
                # get desired result. try to cost down
                right = mid
            else:
                # exceed limit. must upgrade weight limitation
                left = mid + 1
        return left
# @lc code=end

[3,2,2,4,1,4]\n3
[1,2,3,1,1]\n4
