class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(node):
            root = parent[node]
      
            if parent[root] != root:
                parent[node] = find(root)
                return parent[node]
        
            return root

        def union(x, y):
            nonlocal components
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return


            if rank[xRoot] < rank[yRoot]:
                parent[xRoot] = yRoot
            elif rank[yRoot] < rank[xRoot]:
                parent[yRoot] = xRoot
            else:
                parent[yRoot] = xRoot
                rank[xRoot] += 1
            
            components -= 1

        for [frm, to] in edges:
            union(frm, to)

        return components
        
