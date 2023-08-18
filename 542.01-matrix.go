/*
 * @lc app=leetcode id=542 lang=golang
 *
 * [542] 01 Matrix
 */

// @lc code=start
func updateMatrix(mat [][]int) [][]int {
	m, n := len(mat), len(mat[0])
    res := make([][]int, m)
    for i := range res {
        res[i] = make([]int, n)
        for j := range res[i] {
            res[i][j] = math.MaxInt32
        }
    }
    
    q := make([][]int, 0)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 0 {
                res[i][j] = 0
                q = append(q, []int{i, j})
            }
        }
    }
    q = append(q, nil)
    
    shifts := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    visited := make([][]bool, m)
    for i := range visited {
        visited[i] = make([]bool, n)
    }
    
    dist := 1
    for !(len(q) == 1 && len(q[0]) == 0) {
        if len(q[0]) == 0 {
            dist++
            q = q[1:]
            q = append(q, nil)
        }
        
        zero := q[0]
        q = q[1:]
        for _, shift := range shifts {
            x, y := zero[0]+shift[0], zero[1]+shift[1]
            if x < 0 || x >= m || y < 0 || y >= n {
                continue
            }
            if visited[x][y] {
                continue
            }
            if dist < res[x][y] {
                res[x][y] = dist
                q = append(q, []int{x, y})
            }
        }
        visited[zero[0]][zero[1]] = true
    }
    
    return res
}
// @lc code=end

