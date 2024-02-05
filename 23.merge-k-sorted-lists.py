#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        cur = None
        while True:
            minimal_index = None
            for i in range(len(lists)):
                if lists[i] is None:
                    continue

                if minimal_index is None or lists[i].val < lists[minimal_index].val:
                    minimal_index = i

            if minimal_index is None:
                break

            if head is None:
                head = lists[minimal_index]
                cur = head
            else:
                cur.next = lists[minimal_index]
                cur = cur.next

            lists[minimal_index] = lists[minimal_index].next
                
        return head
# @lc code=end

