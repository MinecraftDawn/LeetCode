class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        divisor = divisor << len(format(dividend,'b'))
        quo = 0
        
        for i in range(len(format(dividend,'b'))+1):
            quo = quo << 1
            if divisor <= dividend:
                dividend -= divisor
                quo += 1
            
            divisor = divisor >> 1
        ans = sign * quo
        if ans > 2147483647: ans = 2147483647
        
        return ans