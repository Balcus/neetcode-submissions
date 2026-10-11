# Dijkstra's Algorithm.
# Time Complexity: O(E log V),
# Space Complexity: O(V + E).
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        res = -1
        seen = set()
        minHeap = [(0, k)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in seen:
                continue

            seen.add(node)
            res = max(res, cost)

            for neigh, neighCost in adj[node]:
                if neigh not in seen:
                    heapq.heappush(minHeap, (cost + neighCost, neigh))
                
        return res if len(seen) == n else -1