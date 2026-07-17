class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Rows = len(matrix)
        Cols = len(matrix[0])

        self.sumMat = [[0] * (Cols + 1) for r in range(Rows + 1)]

        for r in range(Rows):
            prefix = 0
            for c in range(Cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1,col1+1,row2+1,col2+1

        bottomLeft = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topleft = self.sumMat[r1-1][c1-1]

        return bottomLeft - left - above + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)