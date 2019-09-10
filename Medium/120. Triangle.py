from operator import add

class Solution:
    def minimumTotal(self, triangle: list) -> int:
        height = len(triangle)
        
        for rowIndex in range(height-1):
            curRow = triangle[rowIndex]
            nextAdd = [2e30] * (rowIndex+2)
            
            for index,val in enumerate(curRow):
                nextAdd[index] = min(nextAdd[index],val)
                nextAdd[index+1] = min(nextAdd[index+1],val)
                
            triangle[rowIndex+1] = list(map(add,triangle[rowIndex+1],nextAdd))
        
        return min(triangle[-1])