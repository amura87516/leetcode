/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> updateMatrix(const vector<vector<int>>& mat) {
        vector<vector<int>> res(mat.size(), vector<int>(mat[0].size(), INT_MAX));
        queue<vector<int>> q;
        // collect all zeros
        // O(m*n)
        for(int i=0;i<mat.size();i++){
            for(int j=0;j<mat[0].size();j++){
                if(mat[i][j] == 0){
                    res[i][j] = 0;
                    q.push(vector<int>{i, j});
                }
            }
        }
        q.push(vector<int>());
        
        // bfs
        // O(m*n)
        vector<vector<bool>> visited(mat.size(), vector<bool>(mat[0].size(), false));
        vector<vector<int>> shifts{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int dist = 1;
        while(!(q.size()==1 && q.front().empty())){
            if(q.front().empty()){
                dist++;
                q.pop();
                q.push(vector<int>());
            }

            vector<int> zero = q.front();
            q.pop();
            for(vector<int> shift: shifts){
                int x = zero[0]+shift[0], y = zero[1]+shift[1];
                if(x < 0 || x>= mat.size() || y < 0 || y >= mat[0].size()) continue;
                if(visited[x][y]) continue;
                if(dist < res[x][y]){
                    res[x][y] = dist;
                    q.push(vector<int>{x, y});
                }
            }
            visited[zero[0]][zero[1]] = true;
        }

        return res;
    }
};
// @lc code=end

