class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        ans = set()
    
        def dfs(string, preIndex, index):
            count = 0
            for i in range(index, len(string)):
                
                if string[i] == "(":
                    count += 1
                elif string[i] == ")":
                    count -= 1
                    if count < 0:
                        for j in range(preIndex, i+1):
                            if string[j] == ")":
                                dfs(s[:j] + s[j+1:], j, index)
                        return
            ans.add(string)
        
        dfs(s, 0, 0)
        return list(ans)