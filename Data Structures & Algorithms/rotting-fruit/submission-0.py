class Solution:
    def isValidIdx(self, i, j, nRows, nCols):
        return i >= 0 and j >= 0 and i < nRows and j < nCols

    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        seen = set()
        q = deque()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # count number of fresh oranges and add rotten oranges to q
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        while q and fresh > 0:
            qLen = len(q)
            for _ in range(qLen):
                (x, y) = q.popleft()
                for (dx, dy) in directions:
                    newX = x + dx
                    newY = y + dy
                    if self.isValidIdx(newX, newY, ROWS, COLS) and (newX, newY) not in seen:
                        seen.add((newX, newY))
                        if grid[newX][newY] == 1:
                            fresh -= 1
                            q.append((newX, newY))
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1
            

