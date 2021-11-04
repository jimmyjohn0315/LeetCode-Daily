class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        m = len(board)
        n = len(board[0])
        dire = [[0,1],[1,0],[1,1]]
        maxsum = [[0] * (n + 1) for _ in range(m + 1)]
        path = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'S':
                    path[i][j] = 1
                elif board[i][j] != 'X':
                    for d in dire:
                        r, c = i + d[0], j + d[1]
                        if path[r][c] == 0:
                            continue
                        if maxsum[r][c] == maxsum[i][j]:
                            path[i][j] += path[r][c]
                        elif maxsum[r][c] > maxsum[i][j]:
                            maxsum[i][j] = maxsum[r][c]
                            path[i][j] = path[r][c]
                            
                    if board[i][j] != 'E':
                        maxsum[i][j] += int(board[i][j])    
        
        return [maxsum[0][0], path[0][0] % mod]
