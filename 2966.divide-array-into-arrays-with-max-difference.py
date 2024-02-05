#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        for num in nums:
            if len(temp) > 0:
                if num - temp[0] <= k:
                    temp.append(num)
                    if len(temp) == 3:
                        res.append(temp)
                        temp = []
                else:
                    return []
            else:
                temp.append(num)
        return res
# @lc code=end
[1,3,3,2,7,3]\n3