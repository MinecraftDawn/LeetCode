from math import log10
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        if n < 10: return 1
        
        hashmap = {1:1}
        ans = 0
        
        for i in range(2,int(log10(n))+1):
            tmp = hashmap[i-1] * 10 + 10**(i-1)
            hashmap[i] = tmp
            
        digit = int(log10(n))                 
            
        while digit:
            powNumber = pow(10, digit)
            num = n // powNumber
            
            if num:
                ans += num * hashmap[digit]
                if num >= 2:
                    ans += powNumber
                else:
                    ans += n - powNumber + 1             
                          
            n -= num * powNumber
            digit -= 1
            
        if n >= 1: ans += 1   
        return ans