class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dire = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = 'A'
            for d in dire:
                dfs(i + d[0], j + d[1])
                
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
