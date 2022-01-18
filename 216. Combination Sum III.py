class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > k * 9:
            return []
        res = []
        path = []
        
        
        def backtracking(start, size, tot):
            if tot > n:
                return
            
            if size == k:
                if tot == n:
                    res.append(path[:])
                return
            
            for i in range(start, 10 - (k - size) + 1):
                path.append(i)
                backtracking(i + 1, size + 1, tot + i)
                path.pop()
                
        backtracking(1, 0, 0)
        return res
