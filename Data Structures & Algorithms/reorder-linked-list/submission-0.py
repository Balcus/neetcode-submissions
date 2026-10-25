# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        sh = slow.next
        slow.next = None
        l2 = self.reverse(sh)

        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr.next.next = l2
            l2 = l2.next
            curr = curr.next.next

        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2

        head.val = dummy.next.val
        head.next = dummy.next.next


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev