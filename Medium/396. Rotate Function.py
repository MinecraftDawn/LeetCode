class Solution:
    def maxRotateFunction(self, A: list) -> int:
        ans = float("-inf")

        ASum = sum(A)
        dp = [self.F(A)]
        for i in range(len(A)):
            curF = dp[-1] + ASum - len(A) * A[-i - 1]
            dp.append(curF)
            ans = max(ans, curF)

        return ans if ans != float("-inf") else 0

    def F(self, A: list):
        value = 0
        for i in range(len(A)):
            value += i * A[i]

        return value