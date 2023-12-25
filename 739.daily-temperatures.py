#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        m = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(m) > 0 and m[-1][0] <= temperatures[i]:
                m = m[:-1]

            if len(m) > 0:
                res[i] = m[-1][1] - i

            m.append((temperatures[i], i))

        return res
# @lc code=end

