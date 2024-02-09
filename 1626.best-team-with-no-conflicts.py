#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # O(nlogn)
        players = list(zip(ages, scores))
        players.sort(key=lambda player: (player[0], player[1]))

        # dp[i] = element[i] compatible with all element in dp[i]
        # if element[j] compatible with element[i], element[j] should compatible with all elelemts in dp[i]
        
        res = 0
        max_score = [player[1] for player in players]
        # O(n^2)
        for i in range(len(players)):
            for j in range(i):
                if players[i][0] == players[j][0] or \
                    players[i][0] > players[j][0] and players[i][1] >= players[j][1]:  
                    max_score[i] = max(max_score[i], max_score[j] + players[i][1])
            res = max(res, max_score[i])
        return res   
# @lc code=end

