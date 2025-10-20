class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        def ship(m):
            load,day=0,1
            for w in weights:
                if load+w>m:
                    day+=1
                    load=0
                load+=w
            return day

        while l<r:
            m=l+(r-l)//2
            day=ship(m)
            if day<=days:
                r=m
            else:
                l=m+1
        return l