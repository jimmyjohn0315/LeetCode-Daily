类似01背包问题：每一个数字有2种选择，+或者-。
如果所有数字总和为sum，加法数字总和为x，那么减法数字总和必定为sum - x
target = x - (sum - x)，得出 x=(target + sum) / 2
问题转化为装满背包容量为x有几种装法
装满背包有几种方法的情况下，递推公式一般为：dp[j] += dp[j - nums[i]]
```python
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
```
