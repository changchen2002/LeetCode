class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(i,j):
            parent[find(i)]=find(j)
        
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
        roots=len({find(i) for i in range(n)})
        return n-roots

