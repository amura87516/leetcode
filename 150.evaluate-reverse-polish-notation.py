#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        index = 0
        while index < len(tokens):
            if tokens[index] in ["+", "-", "*", "/"]:
                if tokens[index] == "+":
                    tokens[index-2] += tokens[index-1]
                elif tokens[index] == "-":
                    tokens[index-2] -= tokens[index-1]
                elif tokens[index] == "*":
                    tokens[index-2] *= tokens[index-1]
                elif tokens[index] == "/":
                    tokens[index-2] /= tokens[index-1]
                tokens = tokens[:index-1] + tokens[index+1:]
                index -= 2
            else:
                tokens[index] = int(tokens[index])
                index += 1

        return tokens[0]
# @lc code=end
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
