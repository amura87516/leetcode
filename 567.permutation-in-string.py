#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = [0] * 26
        for c in s1:
            cnt[ord(c) - ord('a')] += 1
        
        cnt2 = [0] * 26
        for i in range(len(s1)-1):
            cnt2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s1)-1, len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1

            matched = True
            for j in range(26):
                if cnt[j] != cnt2[j]:
                    matched = False
                    break
            if matched:
                return True

            cnt2[ord(s2[i-len(s1)+1]) - ord('a')] -= 1
            
        return False
# @lc code=end
