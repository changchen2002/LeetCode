class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj=defaultdict(list)
        for i,p in enumerate(parent):
            adj[p].append(i)
        
        res=1
        def dfs(cur):
            nonlocal res
            a,b=0,0
            for nei in adj[cur]:
                length=dfs(nei)
                if s[nei]==s[cur]:
                    continue
                if length>a:
                    a,b=length,a
                elif length>b:
                    b=length
            res=max(res,a+b+1)
            return a+1
        dfs(0)
        return res
