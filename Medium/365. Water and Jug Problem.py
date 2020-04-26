from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        
        if x == z or y == z or x + y == z: return True
        
        return not (z % gcd(x,y))