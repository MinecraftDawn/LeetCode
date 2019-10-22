class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        while v1 and v2:
            num1 = int(v1.pop(0))
            num2 = int(v2.pop(0))
            
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
            else:
                continue
            
        while v1:
            num1 = int(v1.pop(0))
            if num1:
                return 1
            
        while v2:
            num2 = int(v2.pop(0))
            if num2:
                return -1
            
        return 0