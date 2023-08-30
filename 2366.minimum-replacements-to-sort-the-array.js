/*
 * @lc app=leetcode id=2366 lang=javascript
 *
 * [2366] Minimum Replacements to Sort the Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumReplacement = function (nums) {
    let res = 0;
    let prev = nums[nums.length - 1]
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] < prev) {
            prev = nums[i]
        } else if (nums[i] > prev) {
            const cnt = Math.ceil(nums[i] / prev)
            res += cnt - 1

            const shortage = prev * cnt - nums[i]
            prev -= Math.ceil(shortage / cnt)
        }
    }
    return res
};
// @lc code=end

