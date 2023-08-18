#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#

# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roadIdsByCity = [[] for _ in range(n)]
        for city, road in enumerate(roads):
            roadIdsByCity[road[0]].append(city)
            roadIdsByCity[road[1]].append(city)
        
        res = 0
        for i in range(n):
            s = set()
            for roadId in roadIdsByCity[i]:
                s.add(roadId)
            for j in range(i+1, n):
                s_temp = s.copy()
                for roadId in roadIdsByCity[j]:
                    s_temp.add(roadId)
                res = max(res, len(s_temp))
        return res
# @lc code=end

