/*
 * @lc app=leetcode id=1615 lang=javascript
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximalNetworkRank = function (n, roads) {
    const roadIdsByCity = Array.from({ length: n }, () => new Array());
    for (let i = 0; i < roads.length; i++) {
        roadIdsByCity[roads[i][0]].push(i)
        roadIdsByCity[roads[i][1]].push(i)
    }

    let res = 0
    for (let i = 0; i < n; i++) {
        const set = new Set()
        for (let roadId of roadIdsByCity[i]) {
            set.add(roadId)
        }
        for (let j = i + 1; j < n; j++) {
            const set_temp = new Set(set)
            for (let roadId of roadIdsByCity[j]) {
                set_temp.add(roadId)
            }
            res = Math.max(res, set_temp.size)
        }
    }
    return res
};
// @lc code=end

