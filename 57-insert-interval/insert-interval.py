class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0]>newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval=[min(intervals[i][0],newInterval[0]), max(intervals[i][1],newInterval[1])]
        res.append(newInterval)
        return res
                
            