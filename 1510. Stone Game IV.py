class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        f = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not f[i - k * k]:
                    f[i] = True
                    break
                k += 1
        
        return f[n]
