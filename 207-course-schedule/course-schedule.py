class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses<2:
            return True
        adj=defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        
        vis=set()
        def dfs(c):
            if c in vis:
                return False
            if adj[c]==[]:
                return True
            vis.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            adj[c]=[]
            vis.remove(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# i    c    p   return 
# 0    0   []   True
# 1    1    4    True   adj[1]=[]
# 2    2    4    True   adj[2]=[]
# 3    3    1    True   
# 3    3    2    True