class Solution:
    def singleNumber(self, nums: list) -> int:
        numDict = {}

        for num in nums:
            if num in numDict:
                if numDict[num] < 2:
                    numDict[num] += 1
                else:
                    numDict.pop(num)
            else:
                numDict[num] = 1
        return list(numDict.keys())[0]