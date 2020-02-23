from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        used = set()
        stack = []
        for char in s:
            count[char] -= 1
            
            if char in used: continue
        
            while stack and stack[-1] > char and count[stack[-1]]:
                top = stack.pop()
                used.remove(top)
                
            stack.append(char)
            used.add(char)
            
        return "".join(stack)