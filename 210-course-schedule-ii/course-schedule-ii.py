class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree=[0]*numCourses
        for cur,pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        res=[]
        while q:
            course=q.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if len(res)==numCourses else []

