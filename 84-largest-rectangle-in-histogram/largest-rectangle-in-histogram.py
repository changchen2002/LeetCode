class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        heights.append(0)
        res=max(heights)
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                res=max(res,height*width)
            stack.append(i)
        return res

