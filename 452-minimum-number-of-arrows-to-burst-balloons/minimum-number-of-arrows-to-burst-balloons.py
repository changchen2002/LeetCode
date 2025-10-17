class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        #[[1,6],[2,8],[7,12][10,16]]
        #[[2,6],[7,12],[10,16]]
        #[2,6],[10,12]
        prev=points[0]
        merge=0
        n=len(points)
        for i in range(1,n):
            if prev[1]>=points[i][0]:
                points[i][0]=max(prev[0],points[i][0])
                points[i][1]=min(prev[1],points[i][1])
                merge+=1
            prev=points[i]
        return n-merge

