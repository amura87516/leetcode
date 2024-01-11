#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        indexes_list = [[0]]
        for i in range(1, len(nums)):
            new_indexes_list = []
            for indexes in indexes_list:
                for j in range(len(indexes)+1):
                    temp = indexes.copy()
                    temp.insert(j, i)
                    new_indexes_list.append(temp)
            indexes_list = new_indexes_list
        
        res = []
        for indexes in indexes_list:
            temp = []
            for index in indexes:
                temp.append(nums[index])
            res.append(temp)
        return res
# @lc code=end

