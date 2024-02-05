#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_maxium = []
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > stack[-1][0]:
                stack = stack[:-1]
            if len(stack) > 0:
                left_maxium.append(stack[-1])
            else:
                left_maxium.append([-1, -1])
            stack.append([height[i], i])
        print(left_maxium)

        right_maxium = []
        stack = []
        for i in range(len(height)-1, -1, -1):
            while len(stack) > 0 and height[i] > stack[-1][0]:
                stack = stack[:-1]
            if len(stack) > 0:
                right_maxium.append(stack[-1])
            else:
                right_maxium.append([-1, -1])
            stack.append([height[i], i])
        right_maxium = right_maxium[::-1]
        print(right_maxium)
            
        left = 0
        right = len(height)-1
        res = (right-left)*min(height[left], height[right])
        while left < right:
            print(res, left, right)
            if left_maxium[right][1] == -1 and right_maxium[left][1] == -1:
                break
            elif left_maxium[right][1] == -1:
                left = right_maxium[left][1]
                res = max(res, (right-left)*min(height[left], height[right]))
            elif right_maxium[left][1] == -1:
                right = left_maxium[right][1]
                res = max(res, (right-left)*min(height[left], height[right]))
            else:
                res1 = (left_maxium[right][1]-left)*min(height[left], height[left_maxium[right][1]])
                res2 = (right-right_maxium[left][1])*min(height[right_maxium[left][1]], height[right])
                print(res1, res2)

                if res1 > res2:
                    right = left_maxium[right][1]
                    res = max(res, res1)
                else:
                    left = right_maxium[left][1]
                    res = max(res, res2)
        print(res, left, right)
        return res
# @lc code=end
[1,2,1]
[1,2]
[6,4,3,1,4,6,99,62,1,2,6]
