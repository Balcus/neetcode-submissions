# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        first = list1
        second = list2

        while first and second:
            if first.val < second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next

        if first:
            tail.next = first
        elif second:
            tail.next = second

        return dummy.next
            

        