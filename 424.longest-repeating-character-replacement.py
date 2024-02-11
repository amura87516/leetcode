#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {s[0]: 1}
        left = 0
        res = s[0]
        most_freq_key = s[0]
        for right in range(1, len(s)):
            # update counter
            if s[right] in counter:
                counter[s[right]] += 1
                if counter[s[right]] > counter[most_freq_key]:
                    most_freq_key = s[right]
            else:
                counter[s[right]] = 1

            # check cnt of non most frequent key less than k
            if (right - left + 1) - counter[most_freq_key] <= k:
                if len(res) < right - left + 1:
                    # print(s[left:right+1])
                    res = s[left:right+1]

            # if not, pop front
            while (right - left + 1) - counter[most_freq_key] > k:
                counter[s[left]] -= 1
                if most_freq_key == s[left]:
                    for key in counter:
                        if counter[key] > counter[most_freq_key]:
                            most_freq_key = key
                left += 1
                
        return len(res)
# @lc code=end
"AABABBA"\n1
"ABAA"\n0
"KRSCD"\n4
