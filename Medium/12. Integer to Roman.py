class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        unit = {1:('I','V','X'),
                2:('X','L','C'),
                3:('C','D','M'),
                4:('M','_','_')}
        
        for i in range(1,5):
            if num == 0:
                return roman
            
            mod = num % 10
            num = num // 10
            
            if mod == 1:
                roman = unit[i][0] + roman
            elif mod == 2:
                roman = mod * unit[i][0] + roman
            elif mod == 3:
                roman = mod * unit[i][0] + roman
            elif mod == 4:
                roman = unit[i][0] + unit[i][1] + roman
            elif mod == 5:
                roman = unit[i][1] + roman
            elif mod == 6:
                roman = unit[i][1] + unit[i][0] + roman
            elif mod == 7:
                roman = unit[i][1] + unit[i][0] * 2 + roman
            elif mod == 8:
                roman = unit[i][1] + unit[i][0] * 3 + roman
            elif mod == 9:
                roman = unit[i][0] + unit[i][2] + roman
            elif mod == 0:
                pass
            
        return roman