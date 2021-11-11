class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(n - 1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                res += profit
                
        return res
