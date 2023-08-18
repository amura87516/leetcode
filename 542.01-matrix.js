/*
 * @lc app=leetcode id=542 lang=javascript
 *
 * [542] 01 Matrix
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
    const res = Array(mat.length).fill([]).map(() => Array(mat[0].length).fill(1e5))
    const queue = [];
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[0].length; j++) {
            if (mat[i][j] == 0) {
                res[i][j] = 0;
                queue.push([i, j]);
            }
        }
    }
    queue.push(null)

    const shifts = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    const visited = Array(mat.length).fill([]).map(() => Array(mat[0].length).fill(false))
    dist = 1
    while (!(queue.length == 1 && queue[0] == null)) {
        if (queue[0] == null) {
            queue.shift()
            queue.push(null)
            dist++;
        }

        const zero = queue.shift()
        for (const shift of shifts) {
            const x = zero[0] + shift[0]
            const y = zero[1] + shift[1]
            if (x < 0 || x >= mat.length || y < 0 || y >= mat[0].length) {
                continue
            }
            if (visited[x][y]) {
                continue
            }
            if (dist < res[x][y]) {
                res[x][y] = dist
                queue.push([x, y])
            }
        }

        visited[zero[0]][zero[1]] = true
    }

    return res;
};
// @lc code=end

