class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[a].append(b)
        
        def dfs(c):
            if c in vis:
                return False
            if adj[c]==[]:
                return True
            vis.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            adj[c]=[]
            vis.remove(c)
            return True
        
        vis=set()
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            