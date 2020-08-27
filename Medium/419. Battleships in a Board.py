class Solution:
    def countBattleships(self, board: list) -> int:
        self.board = board
        ans = 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                ans += self.dfs(row, col)

        return ans

    def dfs(self, row: int, col: int):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return 0
        if self.board[row][col] == '.':
            return 0

        self.board[row][col] = '.'

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(row + i, col + j)

        return 1