class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n=len(cuboids)
        for arr in cuboids:
            arr.sort(reverse=True)
        cuboids.sort(reverse=True)
        dp=[0]*n
        for i in range(n):
            dp[i]=cuboids[i][0]
            for j in range(i):
                if cuboids[i][1]<=cuboids[j][1] and cuboids[i][2]<=cuboids[j][2]:
                    dp[i]=max(dp[i],cuboids[i][0]+dp[j])
        return max(dp)
