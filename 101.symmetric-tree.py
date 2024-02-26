#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.left is None and root.right is None:
            return True 
        elif (root.left is None) ^ (root.right is None):
            return False

        # get val in same level 
        level_end_symbol = -1
        def get_level_val(q):
            res = []
            while q[0] is not level_end_symbol:
                if q[0] is None:
                    res.append(None)
                else:
                    res.append(q[0].val)
                    q.append(q[0].left)
                    q.append(q[0].right)
                q = q[1:]

            q = q[1:]
            q.append(level_end_symbol)

            return q, res

        # BFS
        left_q = [root.left, level_end_symbol]
        right_q = [root.right, level_end_symbol]
        while len(left_q) > 1 and len(right_q) > 1:
            left_q, left_level = get_level_val(left_q)

            right_q, right_level = get_level_val(right_q)
            right_level = right_level[::-1]
        
            if left_level != right_level:
                return False
        return True
# @lc code=end

[1,2,2,null,3,null,3]