class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        preEnd=intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            if start>=preEnd:
                preEnd=end
            else:
                count+=1
        return count