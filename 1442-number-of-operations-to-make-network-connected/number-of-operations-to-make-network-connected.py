class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        adj=defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        def dfs(u):
            vis.add(u)
            for v in adj[u]:
                if v not in vis:
                    vis.add(v)
                    dfs(v)

        comp=0
        for i in range(n):
            if i not in vis:
                comp+=1
                dfs(i)
        return comp-1