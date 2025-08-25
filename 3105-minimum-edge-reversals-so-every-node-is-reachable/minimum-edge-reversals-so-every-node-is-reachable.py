class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append((v,True))
            graph[v].append((u,False))
        
        res=[0]*n

        def dfs(u,parent):
            for v,reverse in graph[u]:
                if v==parent:
                    continue
                dfs(v,u)
                res[u]+=(0 if reverse else 1) +res[v]
        dfs(0,None)

        def update(u,parent):
            for v,reverse in graph[u]:
                if v==parent:
                    continue
                res[v]=res[u]+(1 if reverse else -1)
                update(v,u)
        update(0,None)
        return res