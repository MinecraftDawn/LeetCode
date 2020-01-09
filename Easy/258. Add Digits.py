class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        
        while num > 9:
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp
            
        return num