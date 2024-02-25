#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        stack = []
        cur = 0
        pre_op = "+"
        # O(n)
        for i in range(len(s)+1):
            if i == len(s) or s[i] in ["+", "-", "*", "/"]:
                # s[i] is operator
                if pre_op in ["+", "-"]:
                    if len(stack) == 2:
                        stack = [stack[0] + stack[1]]
                    stack.append(-cur if pre_op == "-" else cur)
                elif pre_op == "*":
                    stack[-1] *= cur
                elif pre_op == "/":
                    is_negative = stack[-1] < 0
                    stack[-1] = abs(stack[-1]) // cur
                    if is_negative:
                        stack[-1] *= -1

                if i != len(s):
                    cur = 0
                    pre_op = s[i]
            else:
                # s[i] is number
                cur *= 10
                cur += int(s[i])

        return sum(stack)
# @lc code=end

