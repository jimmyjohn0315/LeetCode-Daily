class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i, j = 2, 2
        while j < n:
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
