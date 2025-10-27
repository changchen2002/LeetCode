class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        roots=list(range(n))
        friends=0
        def find(x):
            if roots[x]!=x:
                roots[x]=find(roots[x])
            return roots[x]
        
        def union(x,y):
            r1,r2=find(x),find(y)
            if r1==r2:
                return False
            roots[r2]=r1
            return True
        
        for time,x,y in logs:
            if union(x,y):
                friends+=1
                if friends==n-1:
                    return time
        return -1