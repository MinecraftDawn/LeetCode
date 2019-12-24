class Solution:
    def majorityElement(self, nums: list) -> list:
        bound = len(nums) // 3
        found = set()
        numDict = {}
        
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
            if numDict[num] > bound:
                found.add(num)
                
        return list(found)