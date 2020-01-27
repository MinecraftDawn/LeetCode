class Solution:
    def gameOfLife(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        tmp = [[0] * (len(board[0])+2) for _ in range(len(board)+2)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    for x in range(i,i+3):
                        for y in range(j,j+3):
                            tmp[x][y] += 1
                            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if tmp[i+1][j+1] == 3:
                        board[i][j] = 1
                else:
                    if tmp[i+1][j+1] < 3:
                        board[i][j] = 0
                    elif tmp[i+1][j+1] > 4:
                        board[i][j] = 0