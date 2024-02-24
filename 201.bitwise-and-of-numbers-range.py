#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # longest common prefix in binary format
        
        # Solution 1
        # while right > left:
        #     # clear lowest bit whose value is one
        #     right &= (right - 1)
        # return right

        # Solution 2
        # # O(1)
        # start = 31
        # while start >= 0:
        #     temp = int(math.pow(2, start))

        #     # right bit is 1 but left bit is 0
        #     if (left & temp == temp) ^ (right & temp == temp):
        #         return 0

        #     # first bit equal to 1
        #     if left & temp == temp and right & temp == temp:
        #         break
        #     start -= 1

        # # O(1)
        # end = start-1
        # while end >= 0:
        #     temp = int(math.pow(2, end))
        #     if (left & temp == temp) ^ (right & temp == temp):
        #         break
        #     end -= 1
        
        # # O(1)
        # res = 0
        # for i in range(start, end, -1):
        #     temp = int(math.pow(2, i))
        #     if left & temp:
        #         res += temp
        # return res

        # Solution 3
        # try to add number to make 1 to 0
        # check value in range [left, right] after adding result
        temp = left
        step = 0
        one_indexes = []
        while temp > 0:
            if temp & 1 == 1:
                one_indexes.append(step)
            temp >>= 1
            step += 1

        i = 0
        while i < len(one_indexes):
            print(one_indexes[i], int(math.pow(2, one_indexes[i]+1)), (left % int(math.pow(2, one_indexes[i]+1))))
            if left + int(math.pow(2, one_indexes[i]+1)) - (left % int(math.pow(2, one_indexes[i]+1))) <= right:
                del one_indexes[i]
            else:
                i += 1
        
        res = 0
        for index in one_indexes:
            res += int(math.pow(2, index))
        return res
# @lc code=end
1\n2147483647
600000000\n2147483645
1073741824\n2147483647
3\n4