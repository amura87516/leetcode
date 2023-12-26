#
# @lc app=leetcode id=2522 lang=python3
#
# [2522] Partition String Into Substrings With Values at Most K
#

# @lc code=start
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        partition = []
        left = 0
        right = 0
        while right < len(s):
            cur_s = s[left: right+1]
            if int(cur_s) > k:
                if right == left:
                    return -1
                partition.append(s[left: right])
                left = right
            else:
                right += 1

        if right != left:
            partition.append(s[left: right])

        return len(partition)
        
# @lc code=end

