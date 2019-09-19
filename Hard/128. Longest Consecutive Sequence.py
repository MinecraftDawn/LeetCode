class Solution:
    def longestConsecutive(self, nums: list) -> int:
        numsSet = set()
        ans = 0
        
        for i in nums:
            numsSet.add(i)
        
        for i in nums:
            if i-1 not in numsSet:
                count = 0
                while i in numsSet:
                    count += 1
                    i += 1
                ans = max(ans, count)
                
        return ans