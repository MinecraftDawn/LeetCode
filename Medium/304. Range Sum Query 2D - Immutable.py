class NumMatrix:

    def __init__(self, matrix: list):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.dp[row + 1][col + 1] = matrix[row][col] + self.dp[row + 1][col] + self.dp[row][col + 1] - \
                                            self.dp[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]