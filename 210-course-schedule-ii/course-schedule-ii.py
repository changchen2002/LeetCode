class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adj list(pre->course), for pre indegree==0 we take it first,
        #mark pre as vis, for c, if c is vis, return False. else: cou.outdegree-1, if outdegree==0, take it. in the end if outdegree, return False
        if numCourses<2:
            return [0]
        
        adj=defaultdict(list)
        indeg=[0]*numCourses
        for c,p in prerequisites:
            adj[p].append(c)
            indeg[c]+=1

        res=[i for i in range(numCourses) if indeg[i]==0]
        q=deque(res)
        
        while q:
            p=q.popleft()
            for c in adj[p]:
                indeg[c]-=1
                if indeg[c]==0:
                    res.append(c)
                    q.append(c)
        return res if len(res)==numCourses else []

# adj[0]=[1]
# indeg[0]=1
