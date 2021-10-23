class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(words)
        n = len(words[0])
        l = len(target)
        memo = [[-1] * n for _ in range(l)]
        count = [[0] * 26 for _ in range(n)]
        for c in words:
            for i in range(n):
                count[i][ord(c[i]) - ord('a')] += 1
        mod = 10 ** 9 + 7
        
        def dfs(i, start):
            if i == l:
                return 1
            if n - start < l - i:
                return 0
            if memo[i][start] != -1:
                return memo[i][start]
            
            val = count[start][ord(target[i]) - ord('a')] * dfs(i + 1, start + 1)
            val += dfs(i, start + 1)
            memo[i][start] = val % mod
            return memo[i][start] 
           
        return dfs(0, 0)
