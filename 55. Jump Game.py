class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cover = 0
        for i in range(n):
            if i > cover:
                return False
            cover = max(cover, nums[i] + i)
            if cover >= n - 1:
                return True
        #return False
