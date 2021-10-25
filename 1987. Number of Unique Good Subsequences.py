class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [0, 0]
        f = 0
        mod = int(1e9 + 7)
        for c in reversed(binary):
            if c == '0' : f = 1
            dp[int(c)] = (dp[0] + dp[1] + 1) % mod
        return (dp[1] + f) % mod
