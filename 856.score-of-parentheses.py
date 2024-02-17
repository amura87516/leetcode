#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        left = [[-1, 0]] # (index, score)
        for i in range(len(s)):
            if s[i] == "(":
                left.append([i, 0])
            else:
                last_left = left[-1]
                left = left[:-1]

                if last_left[1] == 0:
                    left[-1][1] += last_left[1]+1 
                else:
                    left[-1][1] += last_left[1]*2
        return left[0][1]
# @lc code=end

