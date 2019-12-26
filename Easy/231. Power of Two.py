class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        
        binary = bin(n)[2:]
        for i in range(1,len(binary)):
            if binary[i] != '0':
                return False
        return True