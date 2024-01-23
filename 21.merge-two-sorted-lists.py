#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
                head.next = None
            else:
                head = list2
                list2 = list2.next
                head.next = None
        elif list1 is not None:
            head = list1
            list1 = list1.next
            head.next = None
        elif list2 is not None:
            head = list2
            list2 = list2.next
            head.next = None
        else:
            return head

        cur = head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
                cur.next = None

        while list1 is not None:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
            cur.next = None
            
        while list2 is not None:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
            cur.next = None

        return head
# @lc code=end

