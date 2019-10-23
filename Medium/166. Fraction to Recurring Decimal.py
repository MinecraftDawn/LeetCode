class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator or not denominator: return "0"
        if numerator % denominator == 0: return str(numerator // denominator)
        
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ans = sign + str(numerator//denominator) + "."
        
        remainder = numerator % denominator
        remDict = {}
        digitNum = len(ans)
        
        while remainder:
            remainder %= denominator
            
            if not remainder:
                return ans
            
            if remainder in remDict:
                return ans[:remDict[remainder]] + "(" + ans[remDict[remainder]:] + ")"
            
            remDict[remainder] = digitNum
            remainder *= 10
            digitNum += 1
            
            ans += str(remainder // denominator)
            
        return ans