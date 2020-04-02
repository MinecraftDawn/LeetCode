from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        numFreq = defaultdict(int)
        for num in nums:
            numFreq[num] += 1
            
        ans = sorted(numFreq, key=lambda x:numFreq[x], reverse=True)
        return ans[:k]