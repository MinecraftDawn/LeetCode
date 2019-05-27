class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        for i in range(length):
            if x[i] == x[length-1-i]:
                if i > length-1-i:
                    return True
            else:
                return False