class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = 1

        direction = True
        add = 1
        while n > 1:
            if direction:
                ans += add
            else:
                if n % 2:
                    ans += add
            n //= 2
            add *= 2
            direction = not direction

        return ans