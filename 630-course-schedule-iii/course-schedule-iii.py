class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        total=0
        heap=[]
        for d,end in courses:
            total+=d
            heapq.heappush(heap,-d)
            if total>end:
                total+=heapq.heappop(heap)
        return len(heap)
    