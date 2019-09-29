from collections import defaultdict
class Solution:
    def singleNumber(self, nums: list) -> int:
        numDict = defaultdict(int)

        for num in nums:
            if numDict[num]:
                numDict.pop(num)
            else:
                numDict[num] += 1
        return list(numDict.keys())[0]