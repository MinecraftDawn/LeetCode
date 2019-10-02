class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        self.wordDict = {key:True for key in wordDict}
        self.checked = {}
        return self.recursive(s)
        
    def recursive(self, string):
        if not string: return True

        if string in self.checked:
            return self.checked[string]
        
        for i in range(1, len(string)+1):
            subString = string[:i]
            if subString in self.wordDict:
                print(subString)
                if self.recursive(string[i:]):
                    self.checked[subString] = True
                    return True
                else:
                    self.checked[string[i:]] = False
        self.checked[string] = False
        return False