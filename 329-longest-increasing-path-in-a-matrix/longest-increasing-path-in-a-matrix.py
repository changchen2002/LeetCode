class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        directions=[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):
            if dp[r][c]:
                return dp[r][c]
            add=0
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    add=max(add,dfs(nr,nc))
            dp[r][c]=add+1
            return dp[r][c]
        
        res=0
        for r in range(m):
            for c in range(n):
                res=max(res,dfs(r,c))
        return res