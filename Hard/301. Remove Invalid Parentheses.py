# Reference: https://leetcode.com/problems/remove-invalid-parentheses/discuss/469590/Python-Version-98-100-(Learned-by-most-voted-post-%40dietpepsi-)
class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        ans = set()
    
        def dfs(string, preIndex, index, reverse):
            pair = ("(",")") if not reverse else (")","(")
            count = 0
            for i in range(index, len(string)):
                
                if string[i] == pair[0]:
                    count += 1
                elif string[i] == pair[1]:
                    count -= 1
                    
                    if count < 0:
                        for j in range(preIndex, i+1):
                            if string[j] == pair[1]:
                                dfs(string[:j] + string[j+1:], j, i, reverse)
                        return
                    
            if not reverse:
                dfs(string[::-1], 0, 0, True)
            else:
                ans.add(string[::-1])
        
        dfs(s, 0, 0, False)
        return list(ans)