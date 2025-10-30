class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return list(range(n))
        adj=defaultdict(list)
        indeg=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[v]+=1
            indeg[u]+=1
        
        q=deque([i for i in range(n) if indeg[i]==1])
        vis=set(q)
        while q:
            print(q)
            for _ in range(len(q)):
                cur=q.popleft()
                vis.add(cur)
                for nei in adj[cur]:
                    if nei not in vis:
                        indeg[nei]-=1
                        if indeg[nei]==1:
                            q.append(nei)
            if n-len(vis)<=2:
                return list(q)