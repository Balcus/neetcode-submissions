class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [float('inf')] * n
        dist[src] = 0
        minHeap = [(0, src)]

        while minHeap:
            d, node = heapq.heappop(minHeap)
            
            if d > dist[node]:
                continue

            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    heapq.heappush(minHeap, (dist[v], v))

        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
    
        return {n: d for n, d in enumerate(dist)}
