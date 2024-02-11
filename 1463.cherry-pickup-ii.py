#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])

        # dp[h][w1][w2]: h for height, w1 for osition of robot1 and w2 for osition of robot2
        dp = [[[grid[h][w1] + (grid[h][w2] if w1 != w2 else 0) for w1 in range(width)] for w2 in range(width)] for h in range(height)]
        
        # bottom up
        for h in range(height-2, -1, -1):
            # traverse all posible position of the two robots
            for w1 in range(width):
                for w2 in range(w1, width):
                    # traverse all possible next step of these two robot
                    current = grid[h][w1] + (grid[h][w2] if w1 != w2 else 0)
                    for d1 in range(max(0, w1-1), min(width-1, w1+1)+1):
                        for d2 in range(max(0, w2-1, d1), min(width-1, w2+1)+1):
                            dp[h][w1][w2] = max(dp[h][w1][w2], current + dp[h+1][d1][d2])
        return dp[0][0][width-1]
# @lc code=end

