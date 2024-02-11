#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a%b)

        gcd = get_gcd(len(nums), k%len(nums))
        for start_index in range(gcd):
            temp = (start_index, nums[start_index])
            for _ in range(len(nums)//gcd):
                # cal new index
                new_index = (temp[0]+k+len(nums))%len(nums)
                temp2 = (new_index, nums[new_index])

                # change target value
                nums[new_index] = temp[-1]

                # put modified value to temp for next swapping
                temp = temp2
# @lc code=end
[-1,-100,3,99]\n2
