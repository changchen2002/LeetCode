class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS用递归,BFS用迭代.少部分情况DFS迭代,不会因递归太深导致爆栈
        rows,cols=len(grid),len(grid[0])
        res=0
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        visited=set()

        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        (nr,nc) not in visited and #漏了导致Time Limit Exceeded:一般是剪枝问题
                        grid[nr][nc]=='1'):
                        q.append((nr,nc))
                        visited.add((nr,nc)) #打错rc很致命

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    bfs(r,c)
                    res+=1
        return res

            