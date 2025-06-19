class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        res=0
        rows,cols=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr in range(rows) and 
                    nc in range(cols) and
                    (nr,nc) not in visited and
                    grid[nr][nc]=='1'):
                    dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    dfs(r,c)
                    res+=1
        return res