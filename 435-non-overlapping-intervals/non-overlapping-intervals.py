class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort(key=lambda x:x[0])
        for i in range(1,len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                if intervals[i-1][1]>=intervals[i][1]:
                    res+=1
                else:
                    res+=1
                    intervals[i][1]=intervals[i-1][1]
        return res
