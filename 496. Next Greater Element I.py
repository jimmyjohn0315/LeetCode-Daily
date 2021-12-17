class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        record = {}
        res = [-1] * m
        stack = [0]
        for i in range(1, n):
            while stack and nums2[i] >= nums2[stack[-1]]:
                record[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        
        for i in range(m):
            res[i] = record.get(nums1[i], -1)
            
        return res
        
    # monotone stack
