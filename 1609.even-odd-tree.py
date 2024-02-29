#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root, None]
        level_nodes = []
        is_even_level = True
        while True:
            cur = q[0]
            q = q[1:]

            if cur is None:
                # check odd val and increasing
                if is_even_level:
                    for i in range(len(level_nodes)):
                        if level_nodes[i] & 1 == 0:
                            return False
                        if i != 0 and level_nodes[i-1] >= level_nodes[i]:
                            return False
                else:
                    # check even val and decreasing
                    for i in range(len(level_nodes)):
                        if level_nodes[i] & 1 == 1:
                            return False
                        if i != 0 and level_nodes[i-1] <= level_nodes[i]:
                            return False

                if len(q) == 0:
                    break
                level_nodes = []
                is_even_level = not is_even_level
                q.append(None)
            else:
                level_nodes.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        return True
# @lc code=end

