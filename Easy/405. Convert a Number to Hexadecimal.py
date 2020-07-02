class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            return self.toHex(2 ** 32 + num)

        numMap = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        ans = ""
        while num > 0 or not ans:
            ans = numMap[num % 16] + ans
            num //= 16
        return ans