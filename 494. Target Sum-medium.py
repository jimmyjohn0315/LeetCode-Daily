class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s < abs(target):
            return 0
        if (s + target) % 2 == 1:
            return 0
    
        x = (s + target) // 2
        dp = [0] * (x + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(x, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]  #累加
        return dp[x]
            
           
