class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return sorted(list(map(str, range(1, n + 1))))[k - 1]
