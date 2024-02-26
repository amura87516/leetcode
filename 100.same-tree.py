#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) ^ (q is None):
            return False
        elif p is None and q is None:
            return True
        elif p.val != q.val:
            return False

        if not self.isSameTree(p.left, q.left):
            return False

        if not self.isSameTree(p.right, q.right):
            return False

        return True
# @lc code=end

[1,2]\n[1,null,2]
[1,1]\n[1,null,1]
[5,4,1,null,1,null,4,2,null,2]\n[5,1,4,4,null,1,null,null,2,null,2]