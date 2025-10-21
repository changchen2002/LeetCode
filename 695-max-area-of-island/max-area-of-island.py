class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        res=0
        vis=set()
        def dfs(r,c):
            nonlocal res
            vis.add((r,c))
            cur=1
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in vis and grid[nr][nc]==1:
                    cur+=dfs(nr,nc)
            res=max(res,cur)
            return cur
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    dfs(r,c)
        return res