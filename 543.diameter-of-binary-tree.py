#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if root is None:
                return [0, 0]

            left = postorder(root.left)
            right = postorder(root.right)

            res = [0, 0]
            res[0] = max(left[0], right[0], left[1] + right[1])
            res[1] = max(left[1] + 1, right[1] + 1)
            return res

        return postorder(root)[0]
# @lc code=end

[1,2]