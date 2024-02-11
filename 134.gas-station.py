#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=startclass Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pre_sum = []
        cur = 0
        for i in range(len(gas)):
            cur += gas[i]-cost[i]
            pre_sum.append(cur)

        min_index = 0
        for i in range(len(pre_sum)):
            if pre_sum[i] < pre_sum[min_index]:
                min_index = i

        index = (min_index+1+len(gas)) % len(gas)
        cur = 0
        cnt = 0
        while cnt < len(gas):
            if cur + gas[index] < cost[index]:
                return -1
            cur += gas[index] - cost[index]
            index = (index+1+len(gas)) % len(gas)
            cnt += 1
        return (min_index+1+len(gas)) % len(gas)
# @lc code=end

[2,3,4]\n[3,4,3]
[3,1,1]\n[1,2,2]