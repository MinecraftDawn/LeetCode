class NumMatrix:

    def __init__(self, matrix: list):
        self.dp = []
        for _ in range(len(matrix)): self.dp.append([0])
        
        for i in range(len(matrix)):
            tmp = 0
            for num in matrix[i]:
                tmp += num
                self.dp[i].append(tmp)
        for i in self.dp:
            print(i)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += self.dp[i][col2+1] - self.dp[i][col1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)