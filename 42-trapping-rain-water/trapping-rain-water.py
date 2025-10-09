class Solution:
    def trap(self, height: List[int]) -> int:
        dec=[]
        res=0
        for i,cur in enumerate(height):
            while dec and cur>height[dec[-1]]:
                pre=height[dec.pop()]
                h=min(cur,height[dec[-1]])-pre if dec else 0
                w=i-dec[-1]-1 if dec else i
                res+=h*w
            dec.append(i)
        return res