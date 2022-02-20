def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    self.dfs(grid, r, c)
                    
        return res
    
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        m, n = len(grid), len(grid[0])
        dire = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for [i,j] in dire:
            x = r + i
            y = c + j
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                self.dfs(grid, x, y)
