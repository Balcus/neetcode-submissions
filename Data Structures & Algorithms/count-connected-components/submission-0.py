class Solution:
    def toAdj(self, n, edges):
        adj = {}
        for node in range(n):
            adj[node] = []

        for [frm, to] in edges:
            adj[frm].append(to)
            adj[to].append(frm)

        return adj

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = self.toAdj(n, edges)
        components = 0

        def dfs(node):
            nonlocal seen, adj

            if node in seen:
                return

            seen.add(node)
            for neigh in adj[node]:
                dfs(neigh)

        for node in adj:
            if node not in seen:
                components += 1
                dfs(node)
        
        return components