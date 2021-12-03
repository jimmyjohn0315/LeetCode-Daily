class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = maxp = minp = nums[0]
        
        for i in range(1, n):
            maxf, minf = maxp, minp
            maxp = max(maxf * nums[i], nums[i], minf * nums[i])
            minp = min(minf * nums[i], nums[i], maxf * nums[i])
            res = max(res, maxp)
            
        return res
