class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        adj=defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])

        remain=n
        while remain>2:
            remain-=len(leaves)
            for _ in range(len(leaves)):
                leaf=leaves.popleft()
                nei=adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei])==1:
                    leaves.append(nei)
        return list(leaves)