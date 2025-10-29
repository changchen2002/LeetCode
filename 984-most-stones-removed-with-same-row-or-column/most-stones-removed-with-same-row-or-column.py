class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        roots=list(range(n))
        def find(x):
            if roots[x]!=x:
                roots[x]=find(roots[x])
            return roots[x]
        def union(x,y):
            r1,r2=find(x),find(y)
            roots[r1]=r2
        
        rows,cols={},{}

        for i,(r,c) in enumerate(stones):
            if r in rows:
                union(i,rows[r])
            else:
                rows[r]=i
            if c in cols:
                union(i,cols[c])
            else:
                cols[c]=i
        
        return n-len({find(x) for x in range(n)})
            

