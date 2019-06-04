class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxBrackets = 0
        table = [0] * len(s)
        unuseBrackets = 0
        brackets = 0
        for char in s:
            if char == '(':
                brackets += 1
            else:
                brackets -= 1
                if brackets < unuseBrackets:
                    unuseBrackets = brackets
                    table[brackets] = table[brackets+1] = 0
                else:
                    table[brackets] += 1 + table[brackets+1]
                    
                    table[brackets+1] = 0
                    maxBrackets = max(table[brackets],maxBrackets)
                
        return maxBrackets * 2