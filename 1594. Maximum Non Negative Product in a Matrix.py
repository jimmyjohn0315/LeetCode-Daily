class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        
        # define dp and initialization
        maxrange = [[0] * n for _ in range(m)]
        minrange = [[0] * n for _ in range(m)]
        maxrange[0][0] = minrange[0][0] = grid[0][0]
        for i in range(1, m):
            maxrange[i][0] = minrange[i][0] = maxrange[i-1][0] * grid[i][0]
        for j in range(1, n):
            maxrange[0][j] = minrange[0][j] = maxrange[0][j - 1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    maxrange[i][j] = max(maxrange[i-1][j], maxrange[i][j-1]) * grid[i][j]
                    minrange[i][j] = min(minrange[i-1][j], minrange[i][j-1]) * grid[i][j]
                else:
                    maxrange[i][j] = min(minrange[i-1][j], minrange[i][j-1]) * grid[i][j]
                    minrange[i][j] = max(maxrange[i-1][j], maxrange[i][j-1]) * grid[i][j]
                    
        return maxrange[-1][-1] % mod if maxrange[-1][-1] >=0 else -1
