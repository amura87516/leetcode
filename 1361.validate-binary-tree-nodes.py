#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#
# 0
# 1 2
# 3 4 5 6
# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        shown = [0] * n
        for node in leftChild+rightChild:
            if node == -1:
                continue
            elif shown[node] == 1:
                # print(node)
                return False
            else:
                shown[node] = 1

        root = None
        for i in range(n):
            if shown[i] == 0:
                if root is None:
                    root = i
                else:
                    # print(i)
                    return False

        if root is None:
            return False
        # print(root)

        level = 1
        start = 0
        end = 1
        visited = set([root])
        while(start < n):
            # print(start, min(n, end))
            left_candidates = leftChild[start:min(n, end)]
            for index, candidate in enumerate(left_candidates):
                if candidate == -1:
                    continue
                elif candidate in visited:
                    return False
                else:
                    if index != 0 and leftChild[(index-1)//2] == -1:
                        return False
                    visited.add(candidate)

            right_candidates = rightChild[start:min(n, end)]
            for index, candidate in enumerate(right_candidates):
                if candidate == -1:
                    continue
                elif candidate in visited:
                    return False
                else:
                    if index != 0 and rightChild[(index-1)//2] == -1:
                        return False
                    visited.add(candidate)

            is_all_empty = (len(set(left_candidates+right_candidates)) == 1 and left_candidates[0] == -1)
            is_last_level = (n <= end)

            # print(is_all_empty, is_last_level)
                
            if is_all_empty and not is_last_level:
                return False
            
            start = end
            end += int(math.pow(2, level))
            level += 1

        return True
# @lc code=end

