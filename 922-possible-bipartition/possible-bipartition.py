class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        color={}
        def dfs(node,c):
            if node in color:
                return color[node]==c
            color[node]=c
            for nei in adj[node]:
                if not dfs(nei,1-c):
                    return False
            return True
        
        for node in range(1,n+1):
            if node not in color:
                if not dfs(node,0):
                    return False
        return True
