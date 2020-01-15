class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numSet = set()
        
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
                
        return list(numSet)