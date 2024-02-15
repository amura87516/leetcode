#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [["()"]]
        while len(res) < n:
            new_res = set()
            for prev in res[-1]:
                for i in range(len(prev)):
                    for j in range(i, len(prev)):
                        new_res.add(f"{prev[:i]}({prev[i:j]}){prev[j:]}")
            new_res = list(new_res)
            new_res.sort()
            res.append(new_res)
        return res[n-1]
# @lc code=end

