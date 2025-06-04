class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        p,a=set(),set()
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,visited,preH):
            if((r,c) in visited or
                r not in range(rows) or 
                c not in range(cols) or
                heights[r][c]<preH):
                return
            visited.add((r,c))
            
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])

        for c in range(cols):
            dfs(0,c,p,heights[0][c])
            dfs(rows-1,c,a,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,p,heights[r][0])
            dfs(r,cols-1,a,heights[r][cols-1])
        
        return list(p&a)
