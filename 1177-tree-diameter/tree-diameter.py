class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q=deque([node])
            vis=set()
            edge=-1
            while q:
                edge+=1
                for _ in range(len(q)):
                    node=q.popleft()
                    vis.add(node)
                    for nei in adj[node]:
                        if nei not in vis:
                            q.append(nei)
            return node,edge
        
        n1,e1=bfs(edges[0][0])
        n2,res=bfs(n1)
        return res
        


