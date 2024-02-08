#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        Greedy
        multiply odd number with 2 in the beginning
        keep divide maximal number by 2 and recalculate deviation
        '''
        q = []
        for i in range(len(nums)):
            if nums[i] & 1 == 1:
                nums[i] *= 2
            heappush(q, -nums[i])
        minimal = min(nums)

        res = 5*(10**9)
        while -q[0] & 1 == 0:
            temp = heappop(q) // 2
            minimal = min(minimal, -temp)
            heappush(q, temp)
            res = min(res, -q[0] - minimal)
        return res
# @lc code=end
[4,1,5,20,3]
[2,10,8]
[3,5]