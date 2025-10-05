class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        n=len(s)
        adj=defaultdict(list)
        for u,v in pairs:
            adj[u].append(v)
            adj[v].append(u)
        
        vis=set()
        res=list(s)

        def dfs(u,comp):
            vis.add(u)
            comp.append(u)
            for v in adj[u]:
                if v not in vis:
                    dfs(v,comp)
        for i in range(n):
            comp=[]
            dfs(i,comp)
            chars=sorted([res[j] for j in comp])
            for c,idx in zip(chars,sorted(comp)):
                res[idx]=c
        return "".join(res)
        
        