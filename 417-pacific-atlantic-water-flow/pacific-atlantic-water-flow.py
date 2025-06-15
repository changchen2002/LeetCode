class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        p,a=set(),set()
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        def dfs(r,c,preH,visited):
            if heights[r][c]<preH:
                return
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr in range(rows)and
                    nc in range(cols)and
                    (nr,nc) not in visited):
                    dfs(r+dr,c+dc,heights[r][c],visited)
        
        for r in range(rows):
            dfs(r,0,heights[r][0],p)
            dfs(r,cols-1,heights[r][cols-1],a)

        for c in range(cols):
            dfs(0,c,heights[0][c],p)
            dfs(rows-1,c,heights[rows-1][c],a)

        return list(p&a)
