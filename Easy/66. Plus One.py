class Solution:
    def plusOne(self, digits: list) -> list:
        number = 0
        for i in range(len(digits)):
            number += digits.pop() * 10 ** i
        number += 1
        
        ans = []
        while number != 0:
            ans.insert(0,number % 10)
            number //= 10
            
        return ans