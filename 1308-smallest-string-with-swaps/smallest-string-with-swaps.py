class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        par=[i for i in range(n)]

        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        def union(x,y):
            par[find(x)]=find(y)
        for u,v in pairs:
            union(u,v)
        
        groups=defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        res=list(s)
        for idxs in groups.values():
            chars=sorted([res[i] for i in idxs])
            for i,c in zip(idxs,chars):
                res[i]=c
        return ''.join(res)