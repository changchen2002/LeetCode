class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        end=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            start=intervals[i][0]
            if start<end:
                res+=1
            else:
                end=intervals[i][1]
        return res

            