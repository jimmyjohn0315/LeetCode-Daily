class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num
        
        lowbit = xorsum & (-xorsum)
        x1, x2 = 0, 0
        for num in nums:
            if num & lowbit:
                x1 ^= num
            else:
                x2 ^= num
        
        return [x1, x2]
                
