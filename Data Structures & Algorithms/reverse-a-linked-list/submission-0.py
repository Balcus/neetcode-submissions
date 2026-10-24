# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Reversing a linked list:

        1 -> 2 -> 3 -> 4
        4 -> 3 -> 2 -> 1

        1. we need the previous node and the current node
        2. we want to basically set the current node next to prev
        3. we want to keep a reference to the next node before doing 2.

        1 -> 2 -> 3
        prev cur  |
                  |
                  nxt
        '''

        prev = None
        res = prev
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
