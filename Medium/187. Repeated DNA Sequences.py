class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list:
        words = {}
        ans = []
            
        for i in range(len(s)-9):
            string = s[i:i+10]
            if string in words:
                words[string] += 1
            else:
                words[string] = 1
           
        for k,v in words.items():
            if v > 1:
                ans.append(k)
                
        return ans