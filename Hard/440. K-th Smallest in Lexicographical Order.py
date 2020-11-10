#Reference: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/770352/100-faster-easy-java-solution-with-detail-explnation

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if k == 0: return 0

        cur = 1
        k -= 1

        def countSteps(left, right, n):
            res = 0
            while left <= n or right <= n:
                res += min(n + 1, right) - left
                left *= 10
                right *= 10

            return res

        while k > 0:
            steps = countSteps(cur, cur + 1, n)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur