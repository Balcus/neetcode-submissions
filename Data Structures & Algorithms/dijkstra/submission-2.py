class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        # We initalize the distance with inf for all nodes except the source which we will add the the min heap
        dist = [float('inf')] * n
        dist[src] = 0
        minHeap = [(0, src)]

        # While there are still nodes that we can reach
        while minHeap:
            d, node = heapq.heappop(minHeap)
            
            # If we obtained a greated distance for reaching the node, we skip
            if d > dist[node]:
                continue

            # for each of the node's neighbours, we check wheter it is cheaper to get to that neighbour
            # by first going through node, if so, we update the distance for the neighbour and then add it to the heap
            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    heapq.heappush(minHeap, (dist[v], v))

        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
    
        return {n: d for n, d in enumerate(dist)}
