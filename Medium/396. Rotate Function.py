class Solution:
    def maxRotateFunction(self, A: list) -> int:
        ans = float("-inf")
        for i in range(len(A)):
            ans = max(ans, self.F(A[i:] + A[:i]))

        return ans if ans != float("-inf") else 0

    def F(self, A:list):
        value = 0
        for i in range(len(A)):
            value += i * A[i]

        return value