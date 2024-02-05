#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        left = 0
        right = 0
        counter2 = {}
        res = ""
        while right < len(s):
            # print(s[left:right+1])
            if s[right] in counter:
                if s[right] in counter2:
                    counter2[s[right]] += 1
                else:
                    counter2[s[right]] = 1

            matched = True
            for key in counter:
                if key not in counter2 or counter[key] > counter2[key]:
                    matched = False
                    break
            
            if matched:
                while left < right:
                    if s[left] not in counter:
                        left += 1
                    elif counter2[s[left]] > counter[s[left]]:
                        counter2[s[left]] -= 1
                        left += 1
                    else:
                        break
                
                if res == "" or len(res) > right - left + 1:
                    res = s[left:right+1]

            right += 1

        return res
# @lc code=right
