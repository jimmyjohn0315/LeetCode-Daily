class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        m = len(rides)
        rides.sort(key=lambda x: x[1])
        dp = [0] * m
        dp[0] = rides[0][1] - rides[0][0] + rides[0][2]
        for i in range(1, m):
            earn = rides[i][1] - rides[i][0] + rides[i][2]
            l, r = 0, i - 1
            while l <= r:
                mid = l + (r - l) // 2
                if rides[mid][1] <= rides[i][0]:
                    l = mid + 1
                else:
                    r = mid - 1
            dp[i] = max(dp[i-1], dp[r] + earn)
        return dp[-1]
