class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        indeg=[0]*numCourses
        pre=[set() for _ in range(numCourses)]

        for p,c in prerequisites:
            adj[p].append(c)
            indeg[c]+=1
        q=deque([i for i in range(numCourses) if indeg[i]==0])

        while q:
            p=q.popleft()
            for c in adj[p]:
                pre[c].update(pre[p]|{p})
                indeg[c]-=1
                if indeg[c]==0:
                    q.append(c)
        
        return [p in pre[c] for p,c in queries]
                    