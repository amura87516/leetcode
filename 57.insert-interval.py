#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # def is_overlap(a, b):
        #     return a[0] <= b[0] and b[0] <= a[1] or a[0] <= b[1] and b[1] <= a[1] \
        #         or b[0] <= a[0] and a[0] <= b[1] or b[0] <= a[1] and a[1] <= b[1]

        # def binary_search(intervals, newInterval):
        #     left = 0
        #     right = len(intervals)-1
        #     while left <= right:
        #         mid = (right-left)//2+left
        #         if is_overlap(intervals[mid], newInterval):
        #             return mid
        #         elif newInterval[1] < intervals[mid][0]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return -1

        # intervals.sort()
        # index = binary_search(intervals, newInterval)
        # if index == -1:
        #     res = intervals + [newInterval]
        #     res.sort()
        #     return res

        # overlaps_left = index
        # while overlaps_left > 0 and is_overlap(intervals[overlaps_left-1], newInterval):
        #     overlaps_left -= 1

        # overlaps_right = index
        # while overlaps_right < len(intervals)-1 and is_overlap(intervals[overlaps_right+1], newInterval):
        #     overlaps_right += 1

        # merged_interval = [min(intervals[overlaps_left][0], newInterval[0]), max(intervals[overlaps_right][1], newInterval[1])]
        # return intervals[:overlaps_left] + [merged_interval] + intervals[overlaps_right+1:]

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