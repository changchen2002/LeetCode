class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        nodes=len(adj)
        def dfs(start):
            vis=[-1]*nodes
            vis[start]=0
            q=deque([start])
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if vis[nei]==-1:
                        vis[nei]=vis[node]+1
                        q.append(nei)

            length=max(vis)
            node=vis.index(length)
            return length,node
        _,a=dfs(0)
        res,_=dfs(a)
        return res

        