#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bitwise operation
        # return n > 0 and (n & (n - 1)) == 0

        # exceed python floating point precision
        # return n > 0 and math.log(n, 2).is_integer()

        # loop
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
# @lc code=end

536870912