#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for point in points:
            heappush(q, (point[0]**2 + point[1]**2, point))
        
        res = []
        for i in range(k):
            res.append(heappop(q)[1])
        return res
# @lc code=end

