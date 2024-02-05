#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        is_visited = [False] * len(nums)
        is_visited[0] = True
        for i in range(len(nums)):
            if not is_visited[i]:
                continue
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                is_visited[j] = True
        return is_visited[-1]
# @lc code=end

