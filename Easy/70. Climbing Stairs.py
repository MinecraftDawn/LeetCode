from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        
        step2 = 0  
        for step1 in range(n,-1,-2):
            ans += factorial(step1+step2) // factorial(step1) // factorial(step2)
            step2 += 1
            
        return ans