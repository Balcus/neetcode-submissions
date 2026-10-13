class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = {}
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            if d not in distances:
                distances[d] = [(x, y)]
            else:
                distances[d].append((x, y))

        minHeap = list(distances.keys())
        heapq.heapify(minHeap)
        res = []

        while minHeap:
            if len(res) == k:
                return res
            d = heapq.heappop(minHeap)
            for x, y in distances[d]:
                if len(res) < k:
                    res.append([x, y])
        
        return res
        
        
