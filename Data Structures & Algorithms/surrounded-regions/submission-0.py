class Solution:
    def isValidIndex(self, i, j, rows, cols):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(i,j):
            if (i, j) in seen:
                return
            
            if not self.isValidIndex(i, j, ROWS, COLS):
                return

            if board[i][j] == 'X':
                return

            seen.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return
        
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)

        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen:
                    board[i][j] = 'X'

    

        
