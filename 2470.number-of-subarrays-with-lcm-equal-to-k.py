#
# @lc app=leetcode id=2470 lang=python3
#
# [2470] Number of Subarrays With LCM Equal to K
#

# @lc code=start
class Solution:
    def get_gcd(self, a, b):
        if b == 0:
            return a
        return self.get_gcd(b, a%b)

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        cnt = 0
        for left in range(len(nums)):
            lcm = 1
            for right in range(left, len(nums)):
                gcd = self.get_gcd(lcm, nums[right]) if lcm > nums[right] else self.get_gcd(nums[right], lcm)
                lcm = lcm * nums[right] // gcd
                if lcm == k:
                    cnt += 1
        return cnt
# @lc code=end

