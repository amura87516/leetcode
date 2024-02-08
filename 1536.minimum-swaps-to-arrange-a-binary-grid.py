#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # count right zeros
        right_zero_cnt = []
        for i in range(len(grid)):
            for j in range(len(grid[i])-1, -1, -1):
                if grid[i][j] == 1:
                    right_zero_cnt.append(len(grid[i])-1 - j)
                    break

        # find first valid row sequentially
        res = 0
        for i in range(len(right_zero_cnt)):
            target = len(right_zero_cnt)-1-i
            is_found = False
            for j in range(i, len(right_zero_cnt)):
                if right_zero_cnt[j] >= target:
                    is_found = True
                    for k in range(j, i, -1):
                        right_zero_cnt[k], right_zero_cnt[k-1] = right_zero_cnt[k-1], right_zero_cnt[k]
                        res += 1
                    break
            
            # no valid row, return -1
            if not is_found:
                return -1

        return res
# @lc code=end

[[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
[[1,0,0],[1,1,0],[1,1,1]]
[[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
