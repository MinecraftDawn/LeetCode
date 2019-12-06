from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node:Node, word:str) -> bool:
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