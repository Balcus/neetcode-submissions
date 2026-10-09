class Solution:
    def toAdj(self, n, edges):
        adj = { i:[] for i in range(n) }
        for frm, to in edges:
            adj[frm].append(to)

        return adj

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = self.toAdj(numCourses, prerequisites)

        # There are 3 possible states for a course

        # visited -> the course has been added to output
        # visiting -> the course has not been added to output yet but has been added to current path (cycle detection)
        # unvisited -> the course has not been added to neither output and cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            for neigh in adj[crs]:
                if not dfs(neigh):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output
