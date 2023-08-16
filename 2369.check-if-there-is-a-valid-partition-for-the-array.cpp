/*
 * @lc app=leetcode id=2369 lang=cpp
 *
 * [2369] Check if There is a Valid Partition For The Array
 */

// @lc code=start
class Solution {

// O(n^2)
bool recursive(const vector<int>& nums, int start = 0){
    if(start == nums.size()){
        return true;
    }
    if(nums.size() - start < 2){
        return false;
    }
    // exactly 2 equal elements
    if(nums[start] == nums[start + 1]){
        if(validPartition(nums, start + 2)){
            return true;
        }
    } 
    if(nums.size() - start >= 3){
        // exactly 3 equal elements
        if(nums[start] == nums[start + 1] && nums[start+1] == nums[start + 2]){
            if(validPartition(nums, start + 3)){
                return true;
            }
        }
        // exactly 3 consecutive increasing elements
        else if(nums[start] == nums[start+1]-1 && nums[start+1] == nums[start+2]-1){
            if(validPartition(nums, start + 3)){
                return true;
            }
        }
    }
    return false;
}

// O(n)
bool dp(const vector<int>& nums, int start = 0){
    vector<bool> combo2(nums.size(), false);
    vector<bool> combo3(nums.size(), false);
    vector<bool> consecutive2(nums.size(), false);
    vector<bool> consecutive3(nums.size(), false);
    for(int i=1;i<nums.size();i++){
        if(nums[i-1] == nums[i]){
            combo2[i] = true;
        }
        if(nums[i-1] == nums[i] - 1){
            consecutive2[i] = true;
        }
    }
    for(int i=2;i<nums.size();i++){
        if(nums[i-1] == nums[i] && combo2[i-1]){
            combo3[i] = true;
        }
        if(nums[i-1] == nums[i] - 1 && consecutive2[i-1]){
            consecutive3[i] = true;
        }
    }

    vector<bool> res(nums.size(), false);
    for(int i=1;i<nums.size();i++){
        if(i == 1){
            res[i] = combo2[i];
        }else if(i == 2){
            res[i] = res[i-2] && combo2[i] || combo3[i] || consecutive3[i];
        }else{
            res[i] = res[i-2] && combo2[i] || res[i-3] && combo3[i] || res[i-3] && consecutive3[i];
        }
    }
    return res.back();
}

public:
    bool validPartition(const vector<int>& nums, int start = 0) {
        // return recursive(nums);
        return dp(nums);
    }
};
// @lc code=end

