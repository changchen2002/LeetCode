class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        t,b=0,rows-1
        while t<=b:
            m=t+(b-t)//2
            if matrix[m][0]<=target<=matrix[m][-1]:
                t=m
                break
            if matrix[m][0]<target:
                t=m+1
            else:
                b=m-1
        if t>b:
            return False

        l,r=0,cols-1
        while l<=r:
            m=l+(r-l)//2
            if matrix[t][m]<target:
                l=m+1
            elif matrix[t][m]>target:
                r=m-1
            else:
                return True
        return False
