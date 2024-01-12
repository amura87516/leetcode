#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        intervals = intervals[1:]
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
# @lc code=end

[[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]
[]\n[5,7]
[[1,5]]\n[6,8]
[[1,5]]\n[0,0]