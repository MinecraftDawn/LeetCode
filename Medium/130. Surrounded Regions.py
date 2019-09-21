class Solution:
    def solve(self, board: list ) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        
        self.board = board
        
        O = []
        self.rows = len(board)
        self.cols = len(board[0])
        
        for i in range(self.cols):
            up = board[0][i]
            if up == 'O': O.append((0,i))
            
            down = board[-1][i]
            if down == 'O': O.append((self.rows-1,i))
                
        for i in range(self.rows):
            left = board[i][0]
            if left == 'O': O.append((i,0))

            right = board[i][-1]
            if right == 'O': O.append((i,self.cols-1))
        self.OSet = set()
        
        for i in O: self.dfs(*i)
        
        sub = self.findAllO().difference(self.OSet)
        
        for i in sub:
            y = i[0]
            x = i[1]
            self.board[y][x] = 'X'
            
    def dfs(self, y, x):
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows: return
        
        if self.board[y][x] == 'O' and (y,x) not in self.OSet:
            self.OSet.add((y,x))
            self.dfs(y+1, x)
            self.dfs(y-1, x)
            self.dfs(y, x-1)
            self.dfs(y, x+1)
            
    def findAllO(self) -> set:
        OSet = set()
        for rowIndex,row in enumerate(self.board):
            for colIndex,ele in enumerate(row):
                if ele == 'O':
                    OSet.add((rowIndex,colIndex))
        return OSet