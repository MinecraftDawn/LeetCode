class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        string = ""
        charStack = [[""]]
        numStack = []

        for char in s:
            if char.isdigit():
                num += char

            elif char == '[':
                numStack.append(int(num))
                num = ""

                if string:
                    charStack[-1][-1] += string
                    string = ""

                charStack.append([""])

            elif char == ']':
                if string:
                    charStack[-1][-1] += string
                    string = ""
                charStack[-1][-1] *= numStack.pop()
                tmp = charStack.pop().pop()
                charStack[-1][-1] += tmp

            else:
                string += char

        if string:
            charStack[-1][-1] += string

        return charStack[-1][-1]