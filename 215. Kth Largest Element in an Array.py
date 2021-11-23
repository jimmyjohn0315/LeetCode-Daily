class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            rindex = random.randint(left, right)
            nums[left], nums[rindex] = nums[rindex], nums[left]
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right] = nums[left]
               
            nums[left] = pivot
            return left
            
        
        start, end = 0, len(nums) - 1
        while True:
            index = partition(nums, start, end)
            if index == k - 1:
                return nums[index]
            elif index > k - 1:
                end = index - 1
            else:
                start = index + 1
