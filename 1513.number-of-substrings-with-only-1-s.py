#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        cnt = {}
        left = 0
        right = 0
        combo = 0
        while(right < len(s)):
            while left < len(s) and s[left] == "0":
                left += 1
                right = left

            if right == len(s):
                break

            if s[right] == "1":
                combo += 1
                right += 1
            else:
                if combo in cnt:
                    cnt[combo] += 1
                else:
                    cnt[combo] = 1
                
                left = right + 1
                right = left

                combo = 0
        
        if combo != 0:
            if combo in cnt:
                cnt[combo] += 1
            else:
                cnt[combo] = 1

        
        res = 0
        for combo in cnt:
            res = int((res + (combo+1)*combo//2 * cnt[combo]) % (1e9+7))
        return res
# @lc code=end

