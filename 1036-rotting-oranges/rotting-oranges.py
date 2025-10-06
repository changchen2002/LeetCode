class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh=0
        q=deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        if fresh==0:
            return 0
        time=-1
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        while q:
            time+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
        return time if fresh==0 else -1