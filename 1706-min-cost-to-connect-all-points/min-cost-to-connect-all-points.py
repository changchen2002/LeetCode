class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        vis=set()
        heap=[(0,0)]
        res=0
        cnt=0
        while cnt<n:
            cost,i=heapq.heappop(heap)
            if i in vis:
                continue
            vis.add(i)
            res+=cost
            cnt+=1
            for j in range(n):
                if j not in vis:
                    d=abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1])
                    heapq.heappush(heap,(d,j))
        return res