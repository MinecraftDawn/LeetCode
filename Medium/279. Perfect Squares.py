class Solution:
    def __init__(self):
        self.dict = {}
        
    def numSquares(self, n: int) -> int:
        if n <= 3: return n
        
        square = int(n ** 0.5)
        minNum = n
        for i in range(square,1,-1):
            num = n - i**2
            if num in self.dict:
                value = self.dict[num]
            else:
                value = self.numSquares(n - i**2)
                self.dict[num] = value
            minNum = min(minNum, value)
            
        return minNum + 1