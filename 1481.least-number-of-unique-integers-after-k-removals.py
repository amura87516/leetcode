#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        cnts = list(counter.values())
        cnts.sort()
        for i in range(len(cnts)):
            if cnts[i] <= k:
                k -= cnts[i]
            else:
                return len(cnts) - i
        return 0
# @lc code=end
[4,3,1,1,3,3,2]\n3