from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num).is_integer()