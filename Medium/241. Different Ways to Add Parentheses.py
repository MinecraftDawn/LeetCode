class Solution:
    def diffWaysToCompute(self, s: str) -> list:
        if s.isdigit():
            return [int(s)]
        
        ans = []
        
        for i,char in enumerate(s):
            if not char.isdigit():
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            ans.append(l + r)
                        elif char == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
                            
        return ans