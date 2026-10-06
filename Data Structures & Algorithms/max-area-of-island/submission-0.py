class Solution:
    def isValidIndex(self, i, j, rows, cols):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        maxArea = 0

        def dfs(i, j):
            nonlocal seen

            if (i, j) in seen:
                return 0

            if not self.isValidIndex(i, j, ROWS, COLS) or grid[i][j] == 0:
                return 0

            seen.add((i, j))

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i, j))

        return maxArea
