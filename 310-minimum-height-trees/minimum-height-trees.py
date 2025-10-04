class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        adj=defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        remain=n
        q=deque([i for i in range(n) if len(adj[i])==1])
        while remain>2:
            remain-=len(q)
            for _ in range(len(q)):
                leaf=q.popleft()
                nei=adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei])==1:
                    q.append(nei)
        return list(q)

                
