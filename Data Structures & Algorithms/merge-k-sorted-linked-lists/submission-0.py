# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        '''
        We will use a min heap for the sorting of the k lists
        Take the first node of each list and add it to the min heap, keyed by value and a count variable that is incremented every time we add to the heap in order to break ties
        Get the smallest node in the heap, add it to the result and add to the heap the next node
        Continue unitl the heap is empty.

        Time Complexity: O(klogn)
        Space Complexity: O(k)
        Where:
            k is the total number of lists
            n is the total number of nodes
        '''
        minHeap = []
        count = 0
        for head in lists:
            if head:
                minHeap.append((head.val, count, head))
                count += 1

        heapq.heapify(minHeap)
        dummy = ListNode()
        cur = dummy
        while minHeap:
            value, _, node = heapq.heappop(minHeap)
            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next
            count += 1

            if node.next:
                heapq.heappush(minHeap, (node.next.val, count, node.next))

        return dummy.next