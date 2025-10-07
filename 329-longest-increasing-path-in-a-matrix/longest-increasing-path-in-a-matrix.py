class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        
        def dfs(r,c,prev):
            if r not in range(m) or c not in range(n) or matrix[r][c]<=prev:
                return 0
            if dp[r][c]!=0:
                return dp[r][c]
            best=1
            for dr,dc in directions:
                best=max(best,1+dfs(r+dr,c+dc,matrix[r][c]))
            dp[r][c]=best
            return best

        res=0
        for r in range(m):
            for c in range(n):
                res=max(res,dfs(r,c,float(-inf)))
        return res