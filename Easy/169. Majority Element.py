class Solution:
    def majorityElement(self, nums: list) -> int:
        countDict = {}
        maxCount = (1,nums[0])
        for i in nums:
            if i in countDict:
                countDict[i] += 1
                if countDict[i] > maxCount[0]:
                    maxCount = (countDict[i],i)
            else:
                countDict[i] = 1
                
        return maxCount[1]