class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,res=0,len(height)-1,0
        while l<r:
            water=(r-l)*min(height[l],height[r])
            res=max(res,water)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res