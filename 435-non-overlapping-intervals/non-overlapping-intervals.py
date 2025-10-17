class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        end=float('-inf')
        for s,e in intervals:
            if end>s:
                res+=1
                end=min(end,e)
            else:
                end=e
        return res

# [[1,2][2,3][3,4]]    [1,3]
#    end