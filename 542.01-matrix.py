#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        res = [[1e5 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] is 0:
                    res[i][j] = 0
                    queue.append((i, j))
        queue.append(None)

        dist = 1
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for j in range(len(mat[0]))] for i in range(len(mat))]
        while not (len(queue) == 1 and queue[0] == None):
            if queue[0] == None:
                dist = dist + 1
                queue = queue[1:]
                queue.append(None)

            point = queue[0]
            queue = queue[1:]
            for shift in shifts:
                x = point[0] + shift[0]
                y = point[1] + shift[1]
                if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]):
                    continue
                if visited[x][y]:
                    continue
                if dist < res[x][y]:
                    res[x][y] = dist
                    queue.append((x, y))

            visited[point[0]][point[1]] = True

        return res
# @lc code=end

