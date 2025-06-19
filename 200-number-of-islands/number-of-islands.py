class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        rows,cols=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c):
            grid[r][c]='0'
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr in range(rows) and 
                    nc in range(cols) and
                    grid[nr][nc]=='1'):
                    dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    dfs(r,c)
                    res+=1
        return res