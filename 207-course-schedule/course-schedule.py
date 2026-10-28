class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in prerequisites:
           adj[b].append(a)
        visited=set()
        def dfs(node):
            if not adj[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            adj[node]=[]
            return True
        
        for b in range(numCourses):
            if not dfs(b):
                return False
        return True


            

            
