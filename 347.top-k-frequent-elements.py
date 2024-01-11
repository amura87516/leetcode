#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_by_num = {}
        for num in nums:
            if num in freq_by_num:
                freq_by_num[num] += 1
            else:
                freq_by_num[num] = 1
        
        q = []
        for num, freq in freq_by_num.items():
            heappush(q, (-freq, num))
        
        res = []
        for i in range(k):
            res.append(heappop(q)[1])
        return res
# @lc code=end

