/*
 * @lc app=leetcode id=1615 lang=cpp
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        // O(m)
        vector<vector<int>> roadIdsByIndex(n, vector<int>());
        for(int i=0;i<roads.size();i++){
            const vector<int>& road = roads[i];
            roadIdsByIndex[road[0]].push_back(i);
            roadIdsByIndex[road[1]].push_back(i);
        }

        // O(n(m+n*m)), m = n^2
        // O(nm(n+1)) = O(n^4)
        int res = 0;
        for(int i=0;i<n;i++){
            set<int> s;
            for(const int roadId: roadIdsByIndex[i]){
                s.insert(roadId);
            }
            for(int j=i+1;j<n;j++){
                set<int> s_temp(s.begin(), s.end());
                for(const int roadId: roadIdsByIndex[j]){
                    s_temp.insert(roadId);
                }
                res = max(res, int(s_temp.size()));
            }
        }
        return res;
    }
};
// @lc code=end

