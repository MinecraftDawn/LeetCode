class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            nums += list(str(i))
            
        return nums[n-1]