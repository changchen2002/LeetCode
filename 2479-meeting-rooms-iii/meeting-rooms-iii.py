class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free=list(range(n)) #available rooms
        busy=[] #占用中的meeting
        count=[0]*n

        for s,e in meetings:
            while busy and busy[0][0]<=s:
                end,room=heapq.heappop(busy)
                heapq.heappush(free,room)
            duration=e-s
            if free:
                room=heapq.heappop(free)
                heapq.heappush(busy,(e,room))
            else:
                end,room=heapq.heappop(busy)
                newEnd=end+duration
                heapq.heappush(busy,(newEnd,room))
            count[room]+=1

        mxm=max(count)
        for i,freq in enumerate(count):
            if freq==mxm:
                return i
