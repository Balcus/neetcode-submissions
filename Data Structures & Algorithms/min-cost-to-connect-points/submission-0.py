class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        seen = set()
        x, y = points[0]
        minHeap = [(0, (x, y))]
        res = 0
        points = list(tuple(point) for point in points)

        while minHeap:
            if len(seen) == len(points):
                return res
            
            cost, point = heapq.heappop(minHeap)

            if point in seen:
                continue

            seen.add(point)
            res += cost

            for other in points:
                if other not in seen:
                    distance = abs(other[0] - point[0]) + abs(other[1] - point[1])
                    heapq.heappush(minHeap, (distance, other))

        return res