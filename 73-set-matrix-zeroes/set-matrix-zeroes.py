class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=len(matrix),len(matrix[0])
        visited=set()

        def setZero(r,c):
            visited.add((r,c))
            for row in range(rows):
                if (row,c) not in visited and matrix[row][c]!=0:
                    matrix[row][c]=0
                    visited.add((row,c))
            for col in range(cols):
                if (r,col) not in visited and matrix[r][col]!=0:
                    matrix[r][col]=0
                    visited.add((r,col))

        for r in range(rows):
            for c in range(cols):
                if ((r,c)) not in visited and matrix[r][c]==0:
                    setZero(r,c)

