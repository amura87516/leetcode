#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0 or power < min(tokens):
            return 0

        tokens.sort()

        # greedy grab as much token as you can, O(n)
        score = 0
        pre_sum = [0]
        for token in tokens:
            pre_sum.append(pre_sum[-1] + token)
            if pre_sum[-1] <= power:
                score += 1
        power -= pre_sum[score]
        
        # loop when it can get new token after get power with score, O(n)
        index = score
        while index < len(tokens) and len(tokens) >= 2 and power + tokens[-1] >= tokens[index]:
            # get maximum power with score
            power += tokens[-1] - tokens[index]
            tokens = tokens[1:-1]
            
            # get new token with power as much as you can
            while index < len(tokens) and power >= tokens[index]:
                power -= tokens[index]
                index += 1
                score += 1

        return score
# @lc code=end

[200,100]\n150
[100,200,300,400]\n200
[10,14,70,82]\n4
[29,36,62,64,95]\n72
[26,48,87]\n81
[775, 1099, 1293, 1869, 2262, 2316, 2435, 2913, 3408, 3440, 3591, 3592, 3674, 3739, 3811, 3839, 3843, 3887, 4008, 4011, 4319, 4459, 4709, 4797, 4811, 4866, 4956, 4993, 5002, 5022, 5089, 5135, 5658, 5736, 6180, 6561, 6756, 7423, 7581, 7662, 7785, 8665, 8804, 9158, 9358, 9469, 9558, 9766, 9800, 9930]\n3145