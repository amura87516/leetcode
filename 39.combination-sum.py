#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = set()
        # for candidate in candidates:
        #     if candidate == target:
        #         res.add(tuple([target]))
        #     elif candidate < target:
        #         for temp in self.combinationSum(candidates[i:], target - candidate):
        #             temp = list(temp) + [candidate]
        #             temp.sort()
        #             res.add(tuple(temp))
        # return res
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                res.append([candidates[i]])
            if candidates[i] < target:
                sub_res_list = self.combinationSum(candidates[i:], target - candidates[i])
                for sub_res in sub_res_list:
                    res.append(sub_res + [candidates[i]])
        return res
# @lc code=end

