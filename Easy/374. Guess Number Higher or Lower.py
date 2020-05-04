# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        height = n
        
        while low <= height:
            mid = (low + height) // 2 
            g = guess(mid)
            
            if g == -1:
                height = mid - 1
            elif g == 1:
                low = mid + 1
            else:
                return mid
            
        return height + 1