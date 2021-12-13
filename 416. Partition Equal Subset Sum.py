class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [0] * (s // 2 + 1)
        for i in range(n):
            for j in range(s // 2 , nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[-1] == s // 2
