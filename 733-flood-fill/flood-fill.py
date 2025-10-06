class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        cur=image[sr][sc]
        def dfs(r,c):
            image[r][c]=-1
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==cur:
                    image[nr][nc]=-1
                    dfs(nr,nc)
        
        dfs(sr,sc)
        for r in range(rows):
            for c in range(cols):
                if image[r][c]==-1:
                    image[r][c]=color
        return image