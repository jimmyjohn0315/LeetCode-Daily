class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                prev = i
        
        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2
        
        return count >= n
