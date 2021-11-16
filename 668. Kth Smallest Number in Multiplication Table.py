class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(num):
            count = 0
            for i in range(1, m + 1):
                count += min(num // i, n)
            return count >= k
        
        
        start, end = 1, m * n
        while start < end:
            mid = start + (end - start) // 2
            if check(mid):
                end = mid
            else:
                start = mid + 1
        return end
