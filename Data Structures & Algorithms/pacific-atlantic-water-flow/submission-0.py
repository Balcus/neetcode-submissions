# DFS.
# Time Complexity: O(n * m),
# Space Complexity: O(n * m).

class Solution:
    def isValidIndex(self, i, j, rows, cols):
        return i >=0 and j >= 0 and i < rows and j < cols

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        pacific = set()
        atlantic = set()
        res = []

        def dfs(i, j, idxSet):
            if (i, j) in idxSet:
                return

            idxSet.add((i, j))
            for (dx, dy) in directions:
                newX = i + dx
                newY = j + dy
                if self.isValidIndex(newX, newY, ROWS, COLS) and heights[newX][newY] >= heights[i][j]:
                    dfs(newX, newY, idxSet)

        for j in range(0, COLS):
            dfs(0, j, pacific)
            dfs(ROWS - 1, j, atlantic)

        for i in range(0, ROWS):
            dfs(i, 0, pacific)
            dfs(i, COLS - 1, atlantic)

        for pair in pacific:
            if pair in atlantic:
                res.append(list(pair))

        return res
        

        