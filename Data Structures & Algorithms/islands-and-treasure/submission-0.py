class Solution:
    def isValidIndex(self, i, j, rows, cols):
        return i >=0 and j >= 0 and i < rows and j < cols

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()
        dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    pair = (i, j)
                    seen.add(pair)
                    q.append(pair)

        while q:
            qLen = len(q)
            dist += 1
            for _ in range(qLen):
                x, y = q.popleft()

                for (dx, dy) in directions:
                    newX = x + dx
                    newY = y + dy

                    if not self.isValidIndex(newX, newY, ROWS, COLS):
                        continue

                    if (newX, newY) in seen:
                        continue

                    if grid[newX][newY] == -1:
                        continue
                    
                    seen.add((newX, newY))
                    grid[newX][newY] = dist
                    q.append((newX, newY))
