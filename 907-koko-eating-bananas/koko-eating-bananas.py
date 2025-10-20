class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(x,h):
            for p in piles:
                if p:
                    h-=math.ceil(p/x)
            return h>=0
                
        r=max(piles)
        if r==0:
            return 0
        l=1
        while l<r:
            m=l+(r-l)//2
            if canEat(m,h):
                r=m
            else:
                l=m+1
        return l
