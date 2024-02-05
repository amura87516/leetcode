#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))] 
        dp[0][0] = matrix[0][0]
        for i in range(1, len(matrix)):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for j in range(1, len(matrix[0])):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        # print(dp)
        
        res = 0
        for row in range(len(matrix)):
            for row2 in range(row, len(matrix)):
                cnt = {0: 1}
                for c in range(len(matrix[0])):
                    cur = -(dp[row-1][c] if row > 0 else 0) + dp[row2][c]
                    if cur - target in cnt:
                        res += cnt[cur - target]

                    if cur in cnt:
                        cnt[cur] += 1
                    else:
                        cnt[cur] = 1
        return res
# @lc code=end

[0, 1, 1]
[1, 3, 4]
[1, 4, 5]