#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # O(nlogm)
        left = 0
        right = len(mat[0])-1
        row_index = 0
        while True:
            mid = (right-left)//2+left
            cur_val = mat[row_index][mid]

            left_val = mat[row_index][mid-1] if mid != 0 else -1
            right_val = mat[row_index][mid+1] if mid != len(mat[0])-1 else -1
            top_val = mat[row_index-1][mid] if row_index != 0 else -1
            bottom_val = mat[row_index+1][mid] if row_index != len(mat)-1 else -1

            maximum = max(left_val, right_val, top_val, bottom_val)
            if cur_val > maximum:
                return [row_index, mid]
            elif left_val == maximum:
                right = mid - 1
            elif right_val == maximum:
                left = mid + 1
            elif top_val == maximum:
                row_index -= 1
            elif bottom_val == maximum:
                row_index += 1
        
        # O(nlogm + mlogn)
        # height = len(mat)
        # width = len(mat[0])

        # left = [0] * height
        # right = [width-1] * height
        # top = [0] * width
        # bottom = [height-1] * width

        # mid = [(height-1)//2, (width-1)//2]
        # while True:
        #     cur_val = mat[mid[0]][mid[1]]

        #     left_val = mat[mid[0]][mid[1]-1] if mid[1] != 0 else -1
        #     right_val = mat[mid[0]][mid[1]+1] if mid[1] != width-1 else -1
        #     top_val = mat[mid[0]-1][mid[1]] if mid[0] != 0 else -1
        #     bottom_val = mat[mid[0]+1][mid[1]] if mid[0] != height-1 else -1

        #     maximum = max(left_val, right_val, top_val, bottom_val)

        #     if cur_val > maximum:
        #         return mid
        #     elif left_val == maximum:
        #         right[mid[0]] = mid[1] - 1
        #         mid[1] = (right[mid[0]]-left[mid[0]])//2+left[mid[0]]
        #     elif right_val == maximum:
        #         left[mid[0]] = mid[1] + 1
        #         mid[1] = (right[mid[0]]-left[mid[0]])//2+left[mid[0]]
        #     elif top_val == maximum:
        #         bottom[mid[1]] = mid[0] - 1
        #         mid[0] = (bottom[mid[1]]-top[mid[1]])//2+top[mid[1]]
        #     elif bottom_val == maximum:
        #         top[mid[1]] = mid[0] + 1
        #         mid[0] = (bottom[mid[1]]-top[mid[1]])//2+top[mid[1]]
# @lc code=end
[
    [25,37,23,37,19],
    [45,19,02,43,26],
    [18,01,37,44,50]
    ]
