#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        pq = []
        for i in range(k-1):
            heappush(pq, -nums[i])
            if nums[i] not in cnt:
                cnt[nums[i]] = 1
            else:
                cnt[nums[i]] = cnt[nums[i]] + 1

        res = []
        for i in range(k-1, len(nums)):   
            heappush(pq, -nums[i])
            if nums[i] not in cnt:
                cnt[nums[i]] = 1
            else:
                cnt[nums[i]] = cnt[nums[i]] + 1

            # print(cnt, pq)

            while cnt[-pq[0]] == 0:
                heappop(pq)
            res.append(-pq[0])

            cnt[nums[i-k+1]] = cnt[nums[i-k+1]] - 1

        return res  
            
        
# @lc code=end

