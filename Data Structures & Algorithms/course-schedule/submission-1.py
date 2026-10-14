class Solution:
    def toAdj(self, n, edges):
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)

        return adj

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = self.toAdj(numCourses, prerequisites)
        seen = set()
        curPath = set()

        def dfs(crs):
            if crs in curPath:
                return False
            
            if crs in seen:
                return True

            seen.add(crs)
            curPath.add(crs)

            for neigh in adj[crs]:
                if not dfs(neigh):
                    return False

            curPath.remove(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

            