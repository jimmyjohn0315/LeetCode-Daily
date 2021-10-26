class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            best = float("-inf")
            total = 0
            for j in range(i, n):
                best = max(best, nums[j])
                total += nums[j]
                g[i][j] = best * (j - i + 1) - total
        
        dp = [[float("inf")] * (k + 2) for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 2):
                for i0 in range(i + 1):
                    dp[i][j] = min(dp[i][j], (0 if i0 == 0 else dp[i0 - 1][j - 1]) + g[i0][i])

        return dp[n - 1][k + 1]
