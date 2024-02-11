#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = [None] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if intervals[index]  is None:
                intervals[index] = (i, i)
            else:
                intervals[index] = (min(intervals[index][0], i), max(intervals[index][1], i))
        intervals = [interval for interval in intervals if interval is not None]
        intervals.sort()

        
        def is_overlap(a, b):
            return a[0] <= b[0] and b[0] <= a[1] \
                or a[0] <= b[1] and b[1] <= a[1] \
                or b[0] <= a[0] and a[0] <= b[1] \
                or b[0] <= a[1] and a[1] <= b[1]
        # merge
        index = 0
        while index + 1 < len(intervals):
            if is_overlap(intervals[index], intervals[index+1]):
                intervals[index: index+2] = [(min(intervals[index][0], intervals[index+1][0]), max(intervals[index][1], intervals[index+1][1]))]
            else:
                index += 1
        
        return [interval[1] - interval[0] + 1 for interval in intervals]
# @lc code=end

