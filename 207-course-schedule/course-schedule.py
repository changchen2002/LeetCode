class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adj[course].append(pre)
        
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

        return all(dfs(course)for course in range(numCourses))