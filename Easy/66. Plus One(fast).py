class Solution:
    def plusOne(self, digits: list) -> list:
        for i in range(len(digits)-1,-1,-1):
            digits[i] = (digits[i] + 1) % 10
            
            if digits[i] != 0 : break
            if i == 0: digits.insert(0,1)
            
        return digits