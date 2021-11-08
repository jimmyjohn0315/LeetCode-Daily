class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # the first and its corrresponding index, second small values of each row 
        fs, idx, ss = 0, -1, 0
       
        for i in range(n):
            tfs, tidx, tss = float('inf'), -1, float('inf')
            for j in range(n):
                if j == idx:
                    cur = ss + grid[i][j]
                else:
                    cur = fs + grid[i][j]
                # update smallest values    
                if cur < tfs:
                    tss = tfs
                    tfs = cur
                    tidx = j
                elif cur < tss:
                    tss = cur
            fs, idx, ss = tfs, tidx, tss
        return fs
