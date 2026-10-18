class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        res,i,day=0,0,1
        events.sort()
        hp=[]
        n=len(events)
        
        while i<n or hp:
            if not hp:
                day=max(day,events[i][0])
            while i<n and events[i][0]<=day:
                heapq.heappush(hp,events[i][1])
                i+=1
            while hp and hp[0]<day:
                heapq.heappop(hp)
            if hp:
                heapq.heappop(hp)
                res+=1
                day+=1
        return res


