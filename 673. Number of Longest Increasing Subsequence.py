class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        maxLong = 1
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    elif dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
            if dp[i] == maxLong:
                res += count[i]
            elif dp[i] > maxLong:
                maxLong = dp[i]
                res = count[i]
        return res
