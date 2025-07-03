# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        l,r=1,n
        while l<r:
            m=l+(r-l)//2
            a=isBadVersion(m)
            b=isBadVersion(m+1)
            if not a and b:
                return m+1
            elif a and b:
                r=m
            elif not a and not b:
                l=m+1
        return l


        
