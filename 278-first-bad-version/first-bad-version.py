# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            m=l+(r-l)//2
            if not isBadVersion(m):
                l=m+1
            if isBadVersion(m):
                r=m-1
        return l
