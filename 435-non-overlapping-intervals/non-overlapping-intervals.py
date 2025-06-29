class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res=0
        for i in range(1,len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                res+=1
                intervals[i][1]=intervals[i-1][1]
        return res
