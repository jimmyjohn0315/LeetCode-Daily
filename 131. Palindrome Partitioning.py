class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        
        
        def dfs(start, path):
            if start >= n:
                res.append(path[:])
                return
            for i in range(start, n):
                p = s[start:i + 1]
                if p == p[::-1]:
                    path.append(p) 
                    dfs(i + 1, path)
                    path.pop()
            
        dfs(0, path)
        return res
