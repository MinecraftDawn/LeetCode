# Reference: https://leetcode.com/problems/palindrome-pairs/discuss/535904/Python-3-Clean-Solutions
class Solution:
    def palindromePairs(self, words: list) -> list:
        def palindrome(word:str) -> bool:
            return word == word[::-1]
        
        ans = []
        
        table = {}
        for i, word in enumerate(words):
            table[word] = i
        
        for index, word in enumerate(words):
            for j in range(len(word)+1):
                w1, w2 = word[:j], word[j:]
                if palindrome(w1):
                    rev = w2[::-1]
                    if rev in table and table[rev] != index:
                        ans.append([table[rev], index])
                
                if w2 and palindrome(w2):
                    rev = w1[::-1]
                    if rev in table and table[rev] != index:
                        ans.append([index, table[rev]])
        
        return ans