import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        log = math.log(n,3)
        integer = round(log)
        return abs(integer - log) < 1e-10