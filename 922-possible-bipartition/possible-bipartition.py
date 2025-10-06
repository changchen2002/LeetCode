class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        color=[0]*(n+1)
        def dfs(node,c):
            color[node]=c
            for nei in adj[node]:
                if color[nei]==c:
                    return False
                if color[nei]==0 and not dfs(nei,-c):
                    return False
            return True
        
        for i in range(1,n+1):
            if color[i]==0 and not dfs(i,1):
                return False
        return True
                