class Solution:
    def superPow(self, a: int, b: list) -> int:
        a %= 1337
        ans = 1
        
        for c in b[::-1]:
            ans *= a ** c % 1337
            a = a ** 10 % 1337
            
        return ans % 1337