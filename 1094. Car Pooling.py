class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        p = [0] * 1001
        for t in trips:
            p[t[1]] += t[0]
            p[t[2]] -= t[0]
        
        count = 0
        for i in range(1001):
            count += p[i]
            if count > capacity:
                return False
        return True
