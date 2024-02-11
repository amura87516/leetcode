#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
    
        nums.sort(key=cmp_to_key(lambda a,b: int(b + a) - int(a + b)))

        res = "".join([num for num in nums])

        # remove leading 0
        return str(int(res))
# @lc code=end
[111311, 1113]
[3,30,34,5,9]
