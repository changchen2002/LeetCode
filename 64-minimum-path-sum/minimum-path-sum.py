class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[float('inf')]*cols
        dp[0]=0
        for r in range(rows):
            for c in range(cols):
                if c==0:
                    dp[c]+=grid[r][c]
                else:
                    dp[c]=min(dp[c-1],dp[c])+grid[r][c]
        return dp[-1]