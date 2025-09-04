class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        def getDays(limit):
            day,curr=1,0
            for w in weights:
                if curr+w>limit:
                    day+=1
                    curr=0
                curr+=w
            return day
        while l<r:
            m=l+(r-l)//2
            d=getDays(m)
            if d<=days:
                r=m
            else:
                l=m+1
        return l