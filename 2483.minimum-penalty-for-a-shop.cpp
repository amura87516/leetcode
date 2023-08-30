/*
 * @lc app=leetcode id=2483 lang=cpp
 *
 * [2483] Minimum Penalty for a Shop
 */

// @lc code=start
class Solution {
public:
    // dp
    int bestClosingTime(string customers) {
        vector<int> right_y_cnt(customers.size()+1, 0);
        int cnt = 0;
        for(int i=customers.size()-1;i>=0;i--){
            cnt += customers[i] == 'Y';
            right_y_cnt[i] = cnt;
        }

        int minimum = INT_MAX;
        int res = -1;
        cnt = 0;
        for(int i=0;i<=customers.size();i++){
            int penalty = right_y_cnt[i] + cnt;
            if(minimum > penalty){
                minimum = penalty;
                res = i;
            }
            cnt += customers[i] == 'N';
        }
        return res;
    }
};
// @lc code=end

