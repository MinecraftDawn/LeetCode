class Solution:
    def isHappy(self, n: int) -> bool:
        table = {}
        while n:
            if n in table: return False
            table[n] = False
            
            num = 0
            while n:
                num += (n % 10)**2
                n //= 10
            n = num
            
            if num == 1: return True
        return False