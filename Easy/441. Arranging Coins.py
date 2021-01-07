class Solution:
    def arrangeCoins(self, n: int) -> int:
        self.target = n
        ans = self.binarySearch()
        return ans

    def binarySearch(self) -> int:
        left, leftSigma = 0, 0
        right, rightSigma = self.target, self.sigma(self.target)

        while leftSigma <= rightSigma:
            mid = (left + right) // 2
            midSigma = self.sigma(mid)

            if midSigma > self.target:
                right = mid - 1
                rightSigma = midSigma - mid
            elif midSigma < self.target:
                left = mid + 1
                leftSigma = midSigma + mid + 1
            else:
                return mid

        return right

    def sigma(self, target: int) -> int:
        return (1 + target) * target // 2
