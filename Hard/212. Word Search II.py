from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True
        
    def search(self, word: str) -> bool:
        def dfs(node:TrieNode, word:str) -> bool:
            if not word:
                if node.isWord:
                    return True
            elif word[0] == '.':
                for children in node.children.values():
                    if dfs(children, word[1:]):
                        return True
                else:
                    return False
            else:
                node = node.children.get(word[0])
                if not node: return False
                return dfs(node, word[1:])
        node = self.root
        return dfs(node, word)
   
    def findWords(self, board: list, words: list) -> list:
        if not board or not board[0] or not words:
            return []
        
        ans = []
        rowSize = len(board)
        colSize = len(board[0])
        
        for word in words:
            self.addWord(word)
            
        def dfs(row:int, col:int, node:TrieNode, word:str) -> None:
            
            tmp = board[row][col]
            board[row][col] = ' '
            if node.isWord:
                node.isWord = False
                ans.append(word)
                
            for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                if r < 0 or r >= rowSize or c < 0 or c >= colSize: continue
                if board[r][c] in node.children:
                    char = board[r][c]
                    dfs(r, c, node.children[char], word + char)
            
            board[row][col] = tmp
            
        for rowIndex,row in enumerate(board):
            for colIndex,ele in enumerate(row):
                if ele in self.root.children:
                    dfs(rowIndex, colIndex, self.root.children[ele], ele)
                
        return ans