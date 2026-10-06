class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjList = {}

        for i in range(n):
            adjList[i] = []

        for (frm, to) in edges:
            adjList[frm].append(to)
            adjList[to].append(frm)

        seen = set()

        def dfs(n):
            nonlocal seen

            if n in seen:
                return

            seen.add(n)

            for neigh in adjList[n]:
                dfs(neigh)

        dfs(0)
        return len(seen) == n
        

