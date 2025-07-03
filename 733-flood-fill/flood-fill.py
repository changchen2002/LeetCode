class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start=image[sr][sc]
        if start==color:
            return image

        rows,cols=len(image),len(image[0])
        image[sr][sc]=color
        q=deque([(sr,sc)])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==start:
                    image[nr][nc]=color
                    q.append((nr,nc))
        return image