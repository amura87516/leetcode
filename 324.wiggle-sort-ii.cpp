/*
 * @lc app=leetcode id=324 lang=cpp
 *
 * [324] Wiggle Sort II
 */

// @lc code=start
class Solution {
public:
    int idx(int n, int i) {
        return (1 + 2 * i) % (n | 1);
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        
        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;

        int left = 0, right = n - 1;
        int cur = 0;
        while (cur <= right) {
            if (nums[idx(n, cur)] > mid){
                swap(nums[idx(n, left)], nums[idx(n, cur)]);
                left += 1;
                cur += 1;
            }
            else if (nums[idx(n, cur)] < mid){
                swap(nums[idx(n, cur)], nums[idx(n, right)]);
                right -= 1;
            }
            else
                cur += 1;
        }
    }
    
};
// @lc code=end

