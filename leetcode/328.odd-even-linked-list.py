#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length less than 3
        if head is None or head.next is None or head.next is None:
            return head

        head_even = head.next
        cur_odd = head
        cur_even = head.next
        

        prev = head.next
        cur = head.next.next
        is_odd_index = True
        while cur is not None:
            if is_odd_index:
                cur_odd.next = cur
                cur_odd = cur_odd.next
            else:
                cur_even.next = cur
                cur_even = cur_even.next

            is_odd_index = not is_odd_index
            prev = cur
            cur = cur.next

        cur_odd.next = head_even
        cur_even.next = None
            
        return head

# @lc code=end

[1,2,3,4,5,6,7,8]
[1,2,3,4]
