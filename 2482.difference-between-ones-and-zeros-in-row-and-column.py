#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        top = [[0] * n for _ in range(m)]
        bottom = [[0] * n for _ in range(m)]


        for i in range(m):
            acc = 0
            for j in range(n):
                left[i][j] = acc
                if grid[i][j] == 1:
                    acc += 1

        for i in range(m):
            acc = 0
            for j in range(n-1, -1, -1):
                right[i][j] = acc
                if grid[i][j] == 1:
                    acc += 1

        for j in range(n):
            acc = 0
            for i in range(m):
                top[i][j] = acc
                if grid[i][j] == 1:
                    acc += 1

        for j in range(n):
            acc = 0
            for i in range(m-1, -1, -1):
                bottom[i][j] = acc
                if grid[i][j] == 1:
                    acc += 1

        for i in range(m):
            for j in range(n):
                # onerow = left[i][j] + right[i][j] + (1 if grid[i][j] == 1 else 0)
                # onecol = top[i][j] + bottom[i][j] + (1 if grid[i][j] == 1 else 0)
                # zerorow = (m-1-left[i][j]-right[i][j]) + (1 if grid[i][j] == 0 else 0)
                # zerocol = (n-1-top[i][j]-bottom[i][j]) + (1 if grid[i][j] == 0 else 0)
                # res[i][j] = onerow + onecol - zerorow - zerocol
                
                res[i][j] = (left[i][j] + right[i][j] + top[i][j] + bottom[i][j])*2 + (2 if grid[i][j] == 1 else -2) - m - n + 2
        
        return res

            
        
# @lc code=end

