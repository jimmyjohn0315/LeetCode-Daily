class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        prefix = {0}
        total = 0
        for i in range(n):
            total += nums[i]
            if total - target in prefix:
                res += 1
                prefix.clear()
                total = 0
            prefix.add(total)
        return res
