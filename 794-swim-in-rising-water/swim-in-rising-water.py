class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Dijkstra
        m,n=len(grid),len(grid[0])
        heap=[(grid[0][0],0,0)] # (当前路径最大高度, r, c)
        vis=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            cur,r,c=heapq.heappop(heap)
            if r==m-1 and c==n-1:
                return cur
            if (r,c) in vis:
                continue
            vis.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in vis:
                    heapq.heappush(heap,(max(cur,grid[nr][nc]),nr,nc))
                

