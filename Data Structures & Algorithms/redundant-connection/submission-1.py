class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # In order to implement union find we need parents and rank
        # Initialize parent so that each node is it's own parent at first
        # Initialize rank so that each node has rank 1 at first
        parent = [i for i in range(len(edges))]
        rank = [1] * len(edges)

        # In order to implement find we will need to go up the parent chain unitl we find a node that is his own parent
        # Also added path compression
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        # For union we compare the ranks of the representatives of each node and union based on that
        def union(n1, n2):
            repr1 = find(n1)
            repr2 = find(n2)
            if rank[repr1] == rank[repr2]:
                parent[repr2] = repr1
                rank[repr1] += 1
            elif rank[repr1] < rank[repr2]:
                parent[repr1] = repr2
            else:
                parent[repr2] = repr1
        
        for u, v in edges:
            if find(u - 1) == find(v - 1):
                return [u, v]
            else:
                union(u - 1, v - 1)

            
        