class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[float('inf')] * n for _ in range(n)]
        
        def dfs(start, end):
            if start == end:
                return piles[start]
            if memo[start][end] != float('inf'):
                return memo[start][end]
            startScore = piles[start] - dfs(start + 1, end)
            endScore = piles[end] - dfs(start, end - 1)
            memo[start][end] = max(startScore, endScore)
            return memo[start][end]
        
        return dfs(0, n - 1) > 0
