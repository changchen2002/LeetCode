class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque()
        def bfs(r,c):
            q.append((r,c))
            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                            grid[nr][nc]="0"
                            q.append((nr,nc))
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    res+=1
                    grid[r][c]="0"
                    bfs(r,c)
        return res