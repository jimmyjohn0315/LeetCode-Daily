class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[10001] * (n + 2) for _ in range(m)]
        for j in range(1, n + 1):
            dp[0][j] = matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j-1]
            
        return min(dp[-1])
