class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 4: return True
        n %= 4
        if n == 0: return False
        return True