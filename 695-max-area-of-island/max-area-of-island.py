class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        res=0
        def dfs(r,c):
            nonlocal res
            grid[r][c]=0
            cur=1
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    cur+=dfs(nr,nc)
            res=max(res,cur)
            return cur
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    dfs(r,c)
        return res