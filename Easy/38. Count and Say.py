class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        else:
            preString = self.countAndSay(n-1) + '.'
            count = 1
            string = ''
            for i in range(len(preString)-1):
                if preString[i] == preString[i+1]:
                    count += 1
                else:
                    string += str(count) + preString[i]
                    count = 1
        return string