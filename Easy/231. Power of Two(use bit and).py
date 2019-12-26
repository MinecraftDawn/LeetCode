class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        
        tmp = n & n - 1
        
        return tmp == 0