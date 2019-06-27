class Solution:
    def rotate(self, matrix: list) -> None:
        matrix[::] = zip(*matrix[::-1])