class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def dfs(r1, c1, c2) -> int:
            r2 = r1 + c1 - c2              
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:   
                return float('-inf')
            elif r1 == c1 == n-1:       
                return grid[r1][c1]
            elif dp[r1][c1][c2]  is not None:  
                return dp[r1][c1][c2]
            else:
                res = grid[r1][c1]
                if c1 != c2:
                    res += grid[r2][c2]
                res += max(dfs(r1, c1+1, c2+1), dfs(r1, c1+1, c2), dfs(r1+1, c1, c2), dfs(r1+1, c1, c2+1))
                dp[r1][c1][c2] = res
                return res
                
        return max(0, dfs(0, 0, 0))

