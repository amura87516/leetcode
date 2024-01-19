#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        cur = head
        overflow = (l1.val + l2.val) // 10

        p1 = l1.next
        p2 = l2.next
        while p1 is not None and p2 is not None:
            total = p1.val + p2.val + overflow
            overflow = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            p1 = p1.next
            p2 = p2.next

        while p1 is not None:
            total = p1.val + overflow
            overflow = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            p1 = p1.next

        while p2 is not None:
            total = p2.val + overflow
            overflow = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            p2 = p2.next

        if overflow != 0:
            cur.next = ListNode(overflow)
            
        return head
# @lc code=end

[9,9,9,9,9,9,9]\n[9,9,9,9]