#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counter = [[0, 0] for _ in range(n)] # [outbound, inbound]
        for t in trust:
            counter[t[0]-1][0] += 1
            counter[t[1]-1][1] += 1
        for i in range(n):
            outbound, inbound = counter[i]
            if outbound == 0 and inbound == n-1:
                return i+1
        return -1
# @lc code=end
3\n[[1,3],[2,3]]
3\n[[1,3],[2,3],[3,1]]