#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        for _ in range(a-1):
            cur = cur.next
        temp = cur.next

        # point list[a] to list2[0]
        cur.next = list2

        # move to list1[b]
        for _ in range(b-a):
            temp = temp.next

        # move to list2 tail
        while list2.next is not None:
            list2 = list2.next
        
        # point list2 tail to list1[b]
        list2.next = temp.next

        return list1
# @lc code=end

