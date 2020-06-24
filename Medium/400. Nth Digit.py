from math import ceil
class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = 0
        i = 1
        while nums < n:
            nums += i * 9 * 10 **(i-1)
            i += 1
        i -= 1
        nums -= i * 9 * 10 **(i-1)
        
        n -= nums
        
        t1 = 10**(i-1) + ceil(n / i) - 1
        t2 = (n-1) % i
        
        return int(str(t1)[t2])