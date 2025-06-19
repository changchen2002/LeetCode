class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        for pre,course in prerequisites:
            adj[pre].append(course)
        
        visit=set()
        def dfs(c):
            if adj[c]==[]:
                return True
            if c in visit:
                return False
            visit.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visit.remove(c)
            adj[c]=[]
            return True

        for c in adj.keys():
            if not dfs(c):
                return False
        return True