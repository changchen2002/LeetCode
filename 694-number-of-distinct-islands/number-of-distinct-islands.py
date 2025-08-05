class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        distinct=set()
        def dfs(r,c,orgr,orgc,path):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0:
                return
            grid[r][c]=0
            path.append((r-orgr,c-orgc))
            for dr,dc in directions:
                dfs(r+dr,c+dc,orgr,orgc,path)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    path=[]
                    dfs(r,c,r,c,path)
                    distinct.add(tuple(path))
        return len(distinct)