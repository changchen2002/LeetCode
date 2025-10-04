class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        n=len(graph)
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
        res=[i for i in range(n) if len(graph[i])==0]
        q=deque(res) 
        visit=set() 
        while q:
            des=q.popleft() 
            visit.add(des) 
            for src in adj[des]:
                graph[src].remove(des)
                if len(graph[src])==0 and src not in visit:
                    res.append(src)
                    q.append(src)
        return sorted(res)
        

