class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[[-1,-1]]
        res=0
        for i,height in enumerate(heights):
            while stack[-1][0]!=-1 and stack[-1][0]>height:
                top,idx=stack.pop()
                width=i-stack[-1][1]-1
                res=max(res,top*width)
            stack.append([height,i])
        
        while stack[-1][0]!=-1:
            top,idx=stack.pop()
            width=len(heights)-stack[-1][1]-1
            res=max(res,top*width)

        return res
