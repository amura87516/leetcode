#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for c in s:
            if c == "1":
                cnt += 1
        bits = ["1"] * (cnt-1) + ["0"] * (len(s)-cnt) + ["1"]
        return  "".join(bits)
# @lc code=end