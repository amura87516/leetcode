#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            
            key = 0
            for i in cnt:
                key *= 100
                key += i

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())
# @lc code=end

["bdddddddddd","bbbbbbbbbbc"]