# Reference: https://leetcode.com/problems/self-crossing/discuss/386087/Python-simple-case-easy-to-read
class Solution:
    def isSelfCrossing(self, edge: list) -> bool:
        if len(edge) < 4:
            return False
        
        for i in range(3, len(edge)):
            if edge[i-1] <= edge[i-3] and edge[i] >= edge[i-2]:
                return True
            if i >= 4 and edge[i-1] == edge[i-3] and edge[i] + edge[i-4] >= edge[i-2]:
                return True
            if i >= 5 and edge[i-1] <= edge[i-3] and edge[i-3] <= edge[i-1] + edge[i-5] and edge[i] + edge[i-4] >= edge[i-2] and edge[i-4] <= edge[i-2]:
                return True
            
        return False