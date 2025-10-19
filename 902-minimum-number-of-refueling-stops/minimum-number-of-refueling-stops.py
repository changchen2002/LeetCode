class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        max_heap=[]
        fuel=startFuel
        stop=i=0
        while fuel<target:
            while i<len(stations) and stations[i][0]<=fuel:
                heapq.heappush(max_heap,-stations[i][1])
                i+=1
            if not max_heap:
                return -1
            fuel-=heapq.heappop(max_heap)
            stop+=1
        return stop