/*
 * @lc app=leetcode id=239 lang=javascript
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
    const cnt = new Map();
    const pq = new MaxPriorityQueue();
    for (let i = 0; i < k - 1; i++) {
        if (cnt.has(nums[i])) {
            cnt.set(nums[i], cnt.get(nums[i]) + 1)
        } else {
            cnt.set(nums[i], 1)
        }
        pq.enqueue(nums[i])
    }

    const res = []
    for (let i = k - 1; i < nums.length; i++) {
        if (cnt.has(nums[i])) {
            cnt.set(nums[i], cnt.get(nums[i]) + 1)
        } else {
            cnt.set(nums[i], 1)
        }
        pq.enqueue(nums[i])


        while (cnt.get(pq.front().element) == 0) {
            pq.dequeue();
        }
        res.push(pq.front().element)

        cnt.set(nums[i - k + 1], cnt.get(nums[i - k + 1]) - 1)
    }
    return res;
};
// @lc code=end

