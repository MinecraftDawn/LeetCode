from collections import Counter
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        count = Counter(nums)
        return sorted(count, key=lambda x:count[x], reverse=True)[:k]