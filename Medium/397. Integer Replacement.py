class Solution:
    def __init__(self):
        self.mem = {}

    def integerReplacement(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]

        if n == 1:
            return 0

        if n % 2:
            self.mem[n] = min(self.integerReplacement(n - 1), self.integerReplacement(n + 1)) + 1
            return self.mem[n]
        else:
            self.mem[n] = 1 + self.integerReplacement(n >> 1)
            return self.mem[n]