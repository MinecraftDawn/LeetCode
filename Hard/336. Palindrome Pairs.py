class Solution:
    def palindromePairs(self, words: list) -> list:
        def palindrome(word:str) -> bool:
            if word == word[::-1]:
                return True
            else:
                return False
        
        ans = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and palindrome(words[i]+words[j]):
                    ans.append([i,j])
                    
        return ans