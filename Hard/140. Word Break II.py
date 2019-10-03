class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        self.wordDict = {key:True for key in wordDict}
        self.checked = {}
        self.ans = []
        ans = self.recursive(s)
        return ans
        
    def recursive(self, string:str) -> list:
        if not string: return []
        if string in self.checked: return self.checked[string]
        
        wordList = []
        if string in self.wordDict: wordList.append(string)
        
        for i in range(1, len(string)):
            subString = string[:i]
            
            if subString in self.wordDict:     
                for item in self.recursive(string[i:]):
                    wordList.append(subString + " " + item)
                    
        self.checked[string] = wordList
        return wordList