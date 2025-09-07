class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r=0,n
        while l<=r:
            m=l+(r-l)//2
            coins=m*(m+1)//2 
            if coins==n:
                return m
            elif coins>n:
                r=m-1
            else:
                l=m+1
        return r