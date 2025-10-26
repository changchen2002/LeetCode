class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n<2:
            return informTime[headID]
        
        adj=defaultdict(list)
        for e,m in enumerate(manager):
            if e!=headID:
                adj[m].append(e)

        time=informTime[headID]
        heap=[(time,headID)]
        while heap:
            time,curE=heapq.heappop(heap)
            for sub in adj[curE]:
                heapq.heappush(heap,(time+informTime[sub],sub))
        
        return time
                

        

