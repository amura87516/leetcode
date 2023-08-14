/*
 * @lc app=leetcode id=215 lang=javascript
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
    // solution 1
    // O(nlogk)
    const pq = new MinPriorityQueue();
    for (const num of nums) {
        pq.enqueue(num);
        if (pq.size() > k) {
            pq.dequeue();
        }
    }
    return pq.dequeue().element;

    // // solution 2
    // // O(nlogn)
    // nums.sort((a, b) => a - b);
    // return nums[nums.length - k];
};
// @lc code=end

