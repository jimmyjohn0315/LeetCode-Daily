class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            j = i - 1
            while j >= 0 and i - j <= 10:
                if int(s[j]) != 0 and int(s[j:i]) <= k:
                    dp[i] += dp[j]
                elif int(s[j:i]) > k:
                    break
                j -= 1
            dp[i] %= mod
        return dp[n]
                
    # dp[i] denotes the number of possible arrays ending with s[i-1]
