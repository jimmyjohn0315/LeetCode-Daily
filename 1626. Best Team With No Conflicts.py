class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        players = list(zip(ages, scores))
        players.sort(key=lambda x: (x[0], x[1]))
        dp = [players[i][1] for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            res = max(res, dp[i])
        return res
