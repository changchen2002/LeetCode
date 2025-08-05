class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        heap=[]
        for i in range(len(intervals)):
            start,end=intervals[i][0],intervals[i][1]
            if heap and start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)