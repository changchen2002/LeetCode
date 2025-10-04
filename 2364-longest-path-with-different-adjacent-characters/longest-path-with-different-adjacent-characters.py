class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj=defaultdict(list)
        for i,val in enumerate(parent):
            adj[val].append(i)
        res=1
        def dfs(node):
            nonlocal res
            a=b=0
            for nei in adj[node]:
                cur=dfs(nei)
                if s[nei]==s[node]:
                    continue
                if cur>a:
                    a,b=cur,a
                elif cur>b:
                    b=cur
            res=max(res,a+b+1) 
            return a+1 
        dfs(0)
        return res