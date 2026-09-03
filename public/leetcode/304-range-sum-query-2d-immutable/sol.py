class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.p = [[0] * (n + 1) for _ in range(m + 1)]
        p = self.p
        for i in range(m):
            for j in range(n):
                p[i + 1][j + 1] = p[i + 1][j] + p[i][j + 1] - p[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i, j, k, l = row1, col1, row2, col2
        p = self.p
        return p[k + 1][l + 1] - p[k + 1][j] - p[i][l + 1] + p[i][j]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2,1,4,3)) # 8
print(obj.sumRegion(1,1,2,2)) # 11
print(obj.sumRegion(1,2,2,4)) # 12