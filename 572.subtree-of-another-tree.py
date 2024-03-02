#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (p is None) ^ (q is None):
                return False
            elif p is None and q is None:
                return True
            elif p.val != q.val:
                return False

            if not isSameTree(p.left, q.left):
                return False

            if not isSameTree(p.right, q.right):
                return False

            return True

        if isSameTree(root, subRoot):
            return True

        if root is not None:
            if self.isSubtree(root.left, subRoot):
                return True

            if self.isSubtree(root.right, subRoot):
                return True

        return False
# @lc code=end

[3,4,5,1,2,null,null,null,null,0]\n[4,1,2]
[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]\n[1,null,1,null,1,null,1,null,1,null,1,2]