class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        row=defaultdict(int)
        col=defaultdict(int)
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    row[r]=row.get(r,0)+1
                    col[c]=col.get(c,0)+1
        
        for r in range(rows):
            for c in range(cols):
                if (row[r]>1 or col[c]>1) and grid[r][c]==1:
                    res+=1
                    grid[r][c]=0
        return res