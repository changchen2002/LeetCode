class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 对于某个柱子 heights[i]，
        # 它能向左延伸，直到遇到第一个比它矮的柱子；
        # 也能向右延伸，直到遇到第一个比它矮的柱子。

        stack=[]
        res=0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                res=max(res,height*width)
            stack.append(i)
        return res


