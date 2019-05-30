class Solution:
    
    def generateParenthesis(self, n: int) -> list:
        self.answer = []
        self.size = n
        self.generate([])
        return self.answer

    def generate(self, myList:list):
        if len(myList) < 2 * self.size:
            myList.append('(')
            self.generate(myList.copy())
            myList.pop()
            myList.append(')')
            self.generate(myList.copy())
        else:
            num = 0
            for char in myList:
                if char == '(':
                    num += 1
                else:
                    num -= 1
                    if num < 0:
                        return
            if num == 0:
                self.answer.append(''.join(myList))