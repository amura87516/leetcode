#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n)
        positives = []
        negatives = []
        for num in nums:
            if num >= 0:
                positives.append(num ** 2)
            else:
                negatives.append(num ** 2)
        negatives.reverse()
            

        # O(n)
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(positives) and p2 < len(negatives):
            if positives[p1] <= negatives[p2]:
                res.append(positives[p1])
                p1 += 1
            else:
                res.append(negatives[p2])
                p2 += 1

        while p1 < len(positives):
            res.append(positives[p1])
            p1 += 1
        while p2 < len(negatives):
            res.append(negatives[p2])
            p2 += 1

        return res
# @lc code=end

