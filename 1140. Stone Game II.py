class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        dp = [[-float('inf')] * (n + 1) for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if n - i <= 2 * m:
                    dp[i][m] = suffix[i]
                    continue
                for x in range(1, 2 * m + 1):
                    dp[i][m] = max(dp[i][m], suffix[i] - dp[i + x][max(x, m)])
            
        return dp[0][1]
