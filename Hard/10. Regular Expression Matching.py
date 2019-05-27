import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p += '$'
        match = re.match(p,s)
        if match:
            return True
        else:
            return False