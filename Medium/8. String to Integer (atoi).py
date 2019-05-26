class Solution:
    def myAtoi(self, s: str) -> int:
        answer = ''
        number = '0123456789'
        sign = ''
        
        countSpace = 0
        for char in s:
            if char == ' ':
                countSpace += 1
            else:
                break
          
        s = s[countSpace:]
        
        if len(s) > 0:
            if s[0] == '-':
                sign = '-'
            elif s[0] == '+':
                sign = ''
            elif s[0] not in number:
                return 0
        
        for count,char in enumerate(s):
            if char in number:
                answer += char
            else:
                if count > 0:
                    break;
        if len(answer) == 0: answer = '0'
        answer = int(sign + answer)
        if answer > 2147483647: answer = 2147483647
        if answer < -2147483648: answer = -2147483648
        return answer