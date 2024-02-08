#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for length in range(len(str(low)), len(str(high))+1):
            for iteration in range(1, 9):
                if iteration + length - 1 > 9:
                    continue

                temp = iteration
                while temp // (10 ** (length-1)) < 1:
                    t = temp%10 +1
                    temp *= 10
                    temp += t
                
                if low > temp:
                    continue
                elif temp > high:
                    break
                else:
                    res.append(temp)
        return res
# @lc code=end
1000\n13000