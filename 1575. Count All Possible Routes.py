class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7
        # use memo[i][j] to remember the No. of routes from location i to finish with fuel j
        memo = [[-1] * (fuel + 1) for _ in range(n)]
        def dfs(cur, fuel):
            if memo[cur][fuel] != -1:
                return memo[cur][fuel]
            if fuel <= 0 and cur != finish:
                memo[cur][fuel] = 0
                return 0
            if fuel < abs(locations[cur] - locations[finish]):
                memo[cur][fuel] = 0
                return 0
            if cur == finish:
                memo[cur][fuel] = 1
            else:
                memo[cur][fuel] = 0
            for i in range(n):
                if i == cur:
                    continue
                cost = abs(locations[cur] - locations[i])
                if fuel >= cost:
                    memo[cur][fuel] += dfs(i, fuel - cost)
                    memo[cur][fuel] %= mod
            return memo[cur][fuel]
        
        return dfs(start, fuel)
        
    # DFS + memo
