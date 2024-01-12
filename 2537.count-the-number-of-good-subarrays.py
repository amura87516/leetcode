#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#

# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        cnt = {}
        res = 0
        pair_cnt = 0
        while right < len(nums):
            if nums[right] in cnt:
                pair_cnt -= cnt[nums[right]] * (cnt[nums[right]]-1) // 2
                cnt[nums[right]] += 1
                pair_cnt += cnt[nums[right]] * (cnt[nums[right]]-1) // 2

                # match expectation, update result
                if pair_cnt >= k:
                    res += len(nums) - right

                    while left < right:
                        # eliminate redundant element in front
                        old_left = left
                        pair_cnt -= cnt[nums[old_left]] * (cnt[nums[old_left]]-1) // 2
                        cnt[nums[left]] -= 1
                        left += 1
                        pair_cnt += cnt[nums[old_left]] * (cnt[nums[old_left]]-1) // 2
                        
                        # update result
                        if pair_cnt >= k:
                            res += len(nums) - right
                        else:
                            break

            else:
                cnt[nums[right]] = 1

            right += 1

        return res
# @lc code=end
