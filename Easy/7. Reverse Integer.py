class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            answer *= 10
            answer += x % 10
            x //= 10
        answer *= sign
        if answer > 2147483647 or answer < -2147483648: answer = 0
        return answer