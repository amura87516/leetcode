/*
 * @lc app=leetcode id=2366 lang=cpp
 *
 * [2366] Minimum Replacements to Sort the Array
 */

// @lc code=start
class Solution {
public:
    // greedy from back
    // breakdown all nums larger than next element
    // breakdown to latger number as much as possible
    long long minimumReplacement(vector<int>& nums) {
        long long res = 0;
        int prev = nums[nums.size()-1];
        for(int i=nums.size()-2;i>=0;i--){
            if(nums[i] < prev){
                prev = nums[i];
            }

            // breakdown
            if(nums[i] > prev){
                int cnt = ceil((double) nums[i] / prev); // number of result elements
                res += cnt-1; 
                
                int shortfall = cnt * prev - nums[i]; // shortfall for keep same prev value
                prev = prev - ceil((double)shortfall / cnt); // dispatch shortfall to all new elements
            }
        }
        return res;
    }
};
// @lc code=end
