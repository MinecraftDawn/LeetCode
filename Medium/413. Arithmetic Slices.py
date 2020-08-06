class Solution:
    def numberOfArithmeticSlices(self, A: list) -> int:
        ans = 0
        dp = []
        for i in range(len(A) - 1):
            dp.append(A[i + 1] - A[i])

        dp.append(float("-inf"))
        pre = float("inf")
        count = 0

        for i in range(len(dp)):
            if pre == dp[i]:
                count += 1
            else:
                if count > 1:
                    count -= 1
                    ans += count * (count + 1) // 2

                pre = dp[i]
                count = 1

        return ans