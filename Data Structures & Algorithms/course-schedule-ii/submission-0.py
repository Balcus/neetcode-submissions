class Solution:
    def toAdj(self, n, edges):
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for [frm, to] in edges:
            adj[frm].append(to)

        return adj

    def isAcyclic(self, adj):
        seen = set()
        curPath = set()

        def dfs(i):
            if i in curPath:
                return False

            if i in seen:
                return True

            seen.add(i)
            curPath.add(i)

            for neigh in adj[i]:
                if not dfs(neigh):
                    return False

            curPath.remove(i)

            return True

        for i in adj:
            if not dfs(i):
                return False

        return True


    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = self.toAdj(numCourses, prerequisites)

        if not self.isAcyclic(adj):
            return []

        visited = [False] * numCourses
        res = []

        def dfs(n):
            visited[n] = True
            for neigh in adj[n]:
                if not visited[neigh]:
                    dfs(neigh)
            
            res.append(n)
        
        for i in range(numCourses):
            if not visited[i]:
                dfs(i)

        return res