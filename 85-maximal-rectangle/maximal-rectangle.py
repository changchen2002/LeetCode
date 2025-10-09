class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n=len(matrix),len(matrix[0])
        heights=[0]*(n+1)
        res=0

        for r in range(m):
            for c in range(n):
                if matrix[r][c]=='1':
                    heights[c]+=1
                else:
                    heights[c]=0
            print(heights)
            res=max(res,self.rectangle(heights))
        return res
    
    def rectangle(self,heights:List[int])->int:
        stack=[]
        res=0
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                res=max(res,height*width)
            stack.append(i)
        return res
