/*
 * @lc app=leetcode id=2369 lang=javascript
 *
 * [2369] Check if There is a Valid Partition For The Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function (nums) {
    const combo2 = Array(nums.length).fill(false)
    const combo3 = Array(nums.length).fill(false)
    const consecutive2 = Array(nums.length).fill(false)
    const consecutive3 = Array(nums.length).fill(false)

    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] == nums[i]) {
            combo2[i] = true;
        }
        if (nums[i - 1] == nums[i] - 1) {
            consecutive2[i] = true;
        }
    }

    for (let i = 1; i < nums.length; i++) {
        if (combo2[i - 1] && nums[i - 1] == nums[i]) {
            combo3[i] = true;
        }
        if (consecutive2[i - 1] && nums[i - 1] == nums[i] - 1) {
            consecutive3[i] = true;
        }
    }

    const res = Array(nums.length).fill(false);
    res[1] = combo2[1];
    if (nums.length > 2) {
        res[2] = combo3[2] || consecutive3[2];
    }
    for (let i = 3; i < nums.length; i++) {
        res[i] = (res[i - 2] && combo2[i]) || (res[i - 3] && combo3[i]) || (res[i - 3] && consecutive3[i]);
    }

    return res[nums.length - 1];
};
// @lc code=end

