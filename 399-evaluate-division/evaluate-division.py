class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(dict) #这种双层两个key的是dict
        for (x,y),v in zip(equations,values):
            adj[x][y]=v
            adj[y][x]=1/v
        
        memo={}
        def bfs(src,des):
            if (src,des) in memo:
                return memo[(src,des)]
            if src not in adj or des not in adj:
                return -1.0
            if src==des:
                return 1.0
            
            q=deque([(src,1.0)])
            vis=set([src])
            while q:
                cur,v=q.popleft()
                if cur==des:
                    memo[(src,cur)]=v
                    memo[(cur,src)]=1/v
                    return v
                for nei,val in adj[cur].items():
                    if nei not in vis:
                        vis.add(nei)
                        q.append((nei,v*val))

            memo[(src,des)]=-1.0
            return memo[(src,des)] 

        return [bfs(src,des) for (src,des) in queries]       

