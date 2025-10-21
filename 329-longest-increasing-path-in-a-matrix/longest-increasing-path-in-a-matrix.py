class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        directions=[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):
            if dp[r][c]:
                return dp[r][c]
            cur=1
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    cur=max(cur,1+dfs(nr,nc))
            dp[r][c]=cur
            return cur
        
        res=0
        for r in range(m):
            for c in range(n):
                res=max(res,dfs(r,c))
        return res

# r,c      cur         add         dp[r][c]   
# 2,1       4           3          dp[2][1]=4
# 2,0       3            2         dp[2][0]=3
# 1,0       2           1          dp[1,0]=2     
# 0,0       1          0           dp[0][0]=1