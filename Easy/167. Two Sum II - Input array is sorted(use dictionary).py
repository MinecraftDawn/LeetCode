class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        numDict = {value:index for index,value in enumerate(numbers)}
        
        for index1,i in enumerate(numbers):
            if target-i in numDict:
                return [index1+1,numDict[target-i]+1]