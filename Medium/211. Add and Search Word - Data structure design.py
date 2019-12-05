from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.word[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word in self.word[len(word)]:
            return True
        
        for w in self.word[len(word)]:
            find = True
            for index, char in enumerate(word):
                if char != '.' and char != w[index]:
                    find = False
            if find:
                return True
        return False