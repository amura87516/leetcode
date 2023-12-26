#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split():
            valid = True
            for letter in brokenLetters:
                if letter in word:
                    valid = False
                    break

            if valid:
                res += 1

        return res
# @lc code=end

