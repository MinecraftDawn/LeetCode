class Solution:
    def singleNumber(self, nums: list) -> int:
        numDict = {}

        for num in nums:
            if num in numDict:
                numDict.pop(num)
            else:
                numDict[num] = 1
        return list(numDict.keys())[0]