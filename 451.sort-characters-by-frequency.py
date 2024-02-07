#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        # O(n)
        freq = [0] * (2**8)
        for c in s:
            freq[ord(c)] += 1

        # O(nlogn)
        h = []
        for i in range((2**8)):
            if freq[i]:
                heappush(h, (-freq[i], chr(i)))
        
        # O(n)
        res = []
        while len(h):
            for _ in range(-h[0][0]):
                res.append(h[0][1])
            heappop(h)
        return "".join(res)
# @lc code=end

