#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        level = 1
        while 5 ** level <= n:
            res += (n // (5 ** level))
            level += 1
        return res
# @lc code=end

10000