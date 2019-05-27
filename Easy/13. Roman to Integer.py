class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1,
                  'V':5,
                  'X':10,
                  'L':50,
                  'C':100,
                  'D':500,
                  'M':1000}
        
        preNum = 0
        number = 0
        while len(s) > 0:
            curNum = symbol[s[len(s)-1]]
            s = s[:len(s)-1]
            if curNum >= preNum:
                number += curNum
            else:
                number -= curNum
            preNum = curNum
        return number