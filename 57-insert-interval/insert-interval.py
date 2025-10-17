class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res=[]
        def merge(i1,i2):
            mnm=min(i1[0],i2[0])
            mxm=max(i1[1],i2[1])
            return [mnm,mxm]

        for i,(s,e) in enumerate(intervals):
            if newInterval[1]<s:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            elif newInterval[0]>e:
                res.append(intervals[i])
                if i==len(intervals)-1:
                    res.append(newInterval)
                    return res
                continue
            else:
                newInterval=merge(newInterval,intervals[i])
                if i==len(intervals)-1:
                    res.append(newInterval)
                    return res

#[1,2] [5,6] [3,6]