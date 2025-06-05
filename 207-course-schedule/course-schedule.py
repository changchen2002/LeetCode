class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for c1,c2 in prerequisites:
            adj[c1].append(c2)
        
        visited=set()

        def dfs(c):
            if c in visited:
                return False
            if adj[c]==None:
                return True
            visited.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            adj[c]=None
            visited.remove(c)
            return True
        
        for c,_ in prerequisites:
            if not dfs(c):
                return False
        return True
            
        