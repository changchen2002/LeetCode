class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        hp=[]
        for i,p in enumerate(points):
            d=abs(p[0]**2+p[1]**2)
            heapq.heappush(hp,(-d,i))
            if len(hp)>k:
                heapq.heappop(hp)
        res=[]
        for d,i in hp:
            res.append(points[i])
        return res