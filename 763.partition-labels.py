#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        intervals = intervals[1:]
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res

    def partitionLabels(self, s: str) -> List[int]:
        # convert string to intervals
        interval_by_char = {}
        for i in range(len(s)):
            if s[i] in interval_by_char:
                interval_by_char[s[i]][1] = i
            else:
                interval_by_char[s[i]] = [i, i]

        # merge intervals with binary search
        intervals = list(interval_by_char.values())
        res_intervals = self.merge(intervals)

        # convert intervals to length
        return [interval[1]-interval[0]+1 for interval in res_intervals]
# @lc code=end

