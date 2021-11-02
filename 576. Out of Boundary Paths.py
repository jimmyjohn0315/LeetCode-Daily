class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cache = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        
        def dfs(r, c, k):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if k == 0:
                return 0
            if cache[r][c][k] != -1:
                return cache[r][c][k]
            res = 0
            for d in dire:
                res += dfs(r + d[0], c + d[1], k - 1)
                res %= mod
            cache[r][c][k] = res
            return res
        
        
        return dfs(startRow, startColumn, maxMove)
