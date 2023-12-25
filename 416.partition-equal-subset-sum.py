#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum id odd, no any possible answer
        # O(n)
        total = sum(nums)
        if total & 1 == 1:
            return False

        # expected sum of each partition
        target = total // 2

        # O(nlog(n))
        nums.sort()

        # O(n*nlog(n))
        status = (set(), set())
        for num in nums:
            # no any possible answer if current number larger than expected sum
            if num > target:
                return False
            
            # not select current element, merge previous result
            not_selected = status[0].union(status[1])

            # select current element
            # get partition base on previous result
            selected = set()
            for elelent in not_selected:
                selected.add(num + elelent)
            selected.add(num)

            # found expected partition
            if target in selected:
                return True
            
            # update status
            status = (selected, not_selected)
            
        return False
# @lc code=end

