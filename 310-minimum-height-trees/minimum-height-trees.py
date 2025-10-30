class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return list(range(n))
        adj=defaultdict(list)
        # indeg=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # indeg[v]+=1
            # indeg[u]+=1
        
        q=deque([i for i in range(n) if len(adj[i])==1])
        remain=n
        while remain>2:
            remain-=len(q)
            for _ in range(len(q)):
                cur=q.popleft()
                nei=adj[cur].pop()
                adj[nei].remove(cur)
                if len(adj[nei])==1:
                    q.append(nei)
        return list(q)