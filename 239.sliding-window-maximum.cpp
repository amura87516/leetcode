/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
class Solution {
public:
    // O(nlogn)
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res(nums.size() - k + 1, 0);
        priority_queue<int> pq;
        map<int, int> cnt;
        for(int i=0;i<k-1;i++){
            pq.push(nums[i]);
            cnt[nums[i]] = cnt[nums[i]] + 1;
        }
        for(int i=k-1;i<nums.size();i++){
            // insert new element
            pq.push(nums[i]);
            cnt[nums[i]] = cnt[nums[i]] + 1;

            // get maximum
            while(!cnt[pq.top()]){
                pq.pop();
            }
            res[i-k+1] = pq.top();

            // pop front
            cnt[nums[i-k+1]] = cnt[nums[i-k+1]] - 1;;
        }
        return res;
    }
};
// @lc code=end

