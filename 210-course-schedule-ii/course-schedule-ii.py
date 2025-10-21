class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        out=[0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            out[a]+=1
        
        res=[]
        q=deque([n for n in range(numCourses) if out[n]==0])
        while q:
            pre=q.popleft()
            res.append(pre)
            for course in adj[pre]:
                out[course]-=1
                if out[course]==0:
                    q.append(course)

        return res if len(res)==numCourses else [] 

