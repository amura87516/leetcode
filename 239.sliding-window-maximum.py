#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        cnt = {}
        for i in range(k-1):
            heappush(h, -nums[i])
            if nums[i] in cnt:
                cnt[nums[i]] += 1
            else:
                cnt[nums[i]] = 1

        res = []
        for i in range(k-1, len(nums)):
            # add new element
            heappush(h, -nums[i])
            if nums[i] in cnt:
                cnt[nums[i]] += 1
            else:
                cnt[nums[i]] = 1

            # pop inexist top element in heap
            while -h[0] not in cnt or cnt[-h[0]] == 0:
                heappop(h)
                
            res.append(-h[0])

            # pop front
            cnt[nums[i-k+1]] -= 1

        return res
# @lc code=end