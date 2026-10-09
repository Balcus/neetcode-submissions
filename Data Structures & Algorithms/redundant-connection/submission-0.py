class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        rank = [1] * len(edges)

        def find(x):
            root = parent[x]

            if root != x:
                parent[x] = find(root)
                return parent[x]

            return x

        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return False

            if rank[xRoot] > rank[yRoot]:
                parent[yRoot] = xRoot
            elif rank[xRoot] < rank[yRoot]:
                parent[xRoot] = yRoot
            else:
                parent[yRoot] = xRoot
                rank[xRoot] += 1
            
            return True

        for [frm, to] in edges:
            if not union(frm - 1, to - 1):
                return [frm, to]

            
