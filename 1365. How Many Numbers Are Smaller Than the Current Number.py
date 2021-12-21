class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 102
        for i in nums:
            cnt[i+1] += 1
        for i in range(1, 102):
            cnt[i] += cnt[i-1]
        return [cnt[i] for i in nums]
