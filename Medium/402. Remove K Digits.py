class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return "0"
        if len(num) == k - 1: return min(num)
        if not num: return "0"
        if not k: return num

        # End symbol
        num += ' '
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                break
        num = num[:i] + num[i + 1:]
        return self.removeKdigits(str(int(num)), k - 1)