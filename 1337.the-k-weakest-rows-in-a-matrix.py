#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    cnt += 1
                else:
                    break
            heappush(q, (cnt, i))
        
        res = []
        while len(res) < k and len(q) > 0: 
            res.append(heappop(q)[1])
        return res

# @lc code=end

