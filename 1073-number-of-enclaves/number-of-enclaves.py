class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        lands=0
        q=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    lands+=1
                    if r==0 or r==m-1 or c==0 or c==n-1:
                        q.append((r,c))
                        grid[r][c]=0

        while q:
            r,c=q.popleft()
            lands-=1
            for dr,dc in [[0,1],[0,-1],[-1,0],[1,0]]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    q.append((nr,nc))
                    grid[nr][nc]=0
                    
        return lands

