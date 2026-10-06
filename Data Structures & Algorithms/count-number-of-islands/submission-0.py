class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            nonlocal seen

            if (i, j) in seen:
                return

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == '0':
                return

            seen.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in seen:
                    islands += 1
                    dfs(i, j)

        return islands
            
