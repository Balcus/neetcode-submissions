class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # O(n) to heapify the stones array
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # O(logn) to pop from the heap
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue
            
            # O(logn) to push to the heap
            if x > y:
                heapq.heappush_max(stones, x - y)
            else:
                heapq.heappush_max(stones, y - x)

        return stones[0] if stones else 0