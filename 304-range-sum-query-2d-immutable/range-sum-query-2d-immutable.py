class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.matrix=[[0]*self.n for _ in range(self.m)]
        for r in range(self.m):
            for c in range(self.n):
                self.matrix[r][c]=matrix[r][c]

        self.prefix=[[0]*self.n for _ in range(self.m)]
        for r in range(self.m):
            cur=0
            for c in range(self.n):
                cur+=self.matrix[r][c]
                self.prefix[r][c]=cur
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        for r in range(row1,row2+1):
            if col1>0:
                res+=self.prefix[r][col2]-self.prefix[r][col1-1]
            else:
                res+=self.prefix[r][col2]
        return res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)