#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1

        res = 1
        for i in range(n+1, m+n+1):
            res *= i
        for i in range(2, m+1):
            res //= i
        return res
# @lc code=end

