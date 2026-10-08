# DFS.
# Time Complexity: O(V + E),
# Space Complexity: O(V + E),
# Where V is the number of courses and E is the number of edges.

class Solution:
    def toAdj(self, n, edges):
        adj = {}
        for node in range(n):
            adj[node] = []

        for [frm, to] in edges:
            adj[frm].append(to)

        return adj

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = self.toAdj(numCourses, prerequisites)
        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if adj[course] == []:
                return True

            visited.add(course)
            for neigh in adj[course]:
                if not dfs(neigh):
                    return False

            adj[course] = []
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True