class Solution:
    def numberOfArithmeticSlices(self, A: list) -> int:
        ans = 0
        for i in range(2, len(A)):

            for j in range(1, len(A) - i+1):
                diff = A[j] - A[j - 1]
                for k in range(j+1, j + i):
                    if A[k] - A[k-1] != diff:
                        break
                else:
                    ans += 1

        return ans