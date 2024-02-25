#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#

# @lc code=start
class Solution:
    def distinctNames(self, ideas):
        # dp[i][j]: counter for name that has head i can be changed to head j
        # O(n)
        heads = {ord(idea[0]) - ord('a') for idea in ideas}
        bloom_filter = {idea for idea in ideas}
        
        # O(n)
        counter = [[0] * 26 for _ in range(26)]
        for idea in ideas:
            old_head = ord(idea[0]) - ord('a')
            for new_head in heads:
                modified_idea = chr(new_head + ord('a')) + idea[1:]
                if modified_idea not in bloom_filter:
                    counter[old_head][new_head] += 1
        
        # O(1)
        res = 0
        for i in range(26):
            for j in range(26):
                res += counter[i][j] * counter[j][i]
        return res
# @lc code=end
