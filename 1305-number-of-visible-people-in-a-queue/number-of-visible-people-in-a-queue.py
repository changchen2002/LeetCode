class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n=len(heights)
        dec=[]
        res=[0]*n
        for i in range(n-1,-1,-1):
            if i==n-1:
                dec.append(i)
                continue
            count=0
            while dec and heights[i]>heights[dec[-1]]:
                right=dec.pop()
                count+=1
            res[i]=count+1 if dec else count
            dec.append(i)
        
        return res
        

