from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numList = list(range(1,n+1))
        
        pList = list(permutations(numList))
        
        return ''.join(str(x) for x in pList[k-1])