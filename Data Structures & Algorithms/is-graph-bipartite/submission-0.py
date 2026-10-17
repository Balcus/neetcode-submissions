class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, n1, n2):
        repr1 = self.find(n1)
        repr2 = self.find(n2)

        if repr1 == repr2:
            return False

        if self.rank[repr1] == self.rank[repr2]:
            self.parent[repr2] = repr1
            self.rank[repr1] += 1
        elif self.rank[repr1] < self.rank[repr2]:
            self.parent[repr1] = repr2
        else:
            self.parent[repr2] = repr1

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        uf = UnionFind(len(graph))
        
        for u, neighs in enumerate(graph):
            for v in neighs:
                # If the node is on the same side as it's neighbours then the graph is not bipartite
                if uf.find(u) == uf.find(v):
                    return False

                # Group the neighbours togheter
                uf.union(neighs[0], v)

        return True
        
        