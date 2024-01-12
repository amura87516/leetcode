#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        intervals = intervals[1:]
        cnt = 0
        for interval in intervals:
            if (prev[0] <= interval[0] and interval[0] < prev[1]):
                cnt += 1
                if prev[1] > interval[1]:
                    prev = interval
            else:
                prev = interval
        return cnt
# @lc code=end

[[1,100],[11,22],[1,11],[2,12]]
