#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        for window_size in range(1, len(s)+1):
            for start in range(len(s)-window_size+1):
                if window_size == 1:
                    dp[start][start+window_size-1] = True
                    cnt += 1
                elif window_size in [2, 3]:
                    if s[start] == s[start+window_size-1]:
                        dp[start][start+window_size-1] = True
                        print(s[start:start+window_size])
                        cnt += 1
                elif dp[start+1][start+window_size-2] and s[start] == s[start+window_size-1]:
                    dp[start][start+window_size-1] = True
                    cnt += 1
        return cnt     
# @lc code=end

