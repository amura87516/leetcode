#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # count length of given linked-list
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next

        # move cur to the begining of second-half list
        cur = head
        prev = None
        index = 0
        while index < length / 2:
            prev = cur
            index += 1
            cur = cur.next

        # make node in second-half list point to previous node
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # check palindromic from head and tail
        tail = prev
        index = 0
        while index < length / 2:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next    
            index += 1 
        return True
# @lc code=end

