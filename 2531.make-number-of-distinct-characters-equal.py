#
# @lc app=leetcode id=2531 lang=python3
#
# [2531] Make Number of Distinct Characters Equal
#

# @lc code=startclass Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt = [0] * 26
        keys = set()
        for c in word1:
            cnt[ord(c) - ord('a')] += 1
            keys.add(c)

        cnt2 = [0] * 26
        keys2 = set()
        for c in word2:
            cnt2[ord(c) - ord('a')] += 1
            keys2.add(c)

        for k1 in keys:
            for k2 in keys2:

                cnt[ord(k1) - ord('a')] -= 1
                cnt2[ord(k1) - ord('a')] += 1

                cnt2[ord(k2) - ord('a')] -= 1
                cnt[ord(k2) - ord('a')] += 1

                c1 = 0
                for k in cnt:
                    if k > 0:
                        c1 += 1

                c2 = 0
                for k in cnt2:
                    if k > 0:
                        c2 += 1

                if c1 == c2:
                    return True
                

                cnt2[ord(k1) - ord('a')] -= 1
                cnt[ord(k1) - ord('a')] += 1

                cnt[ord(k2) - ord('a')] -= 1
                cnt2[ord(k2) - ord('a')] += 1
                
        return False
        
# @lc code=end
