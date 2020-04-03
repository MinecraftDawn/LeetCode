from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        count = Counter(nums)
        heap = []
        
        for key,value in count.items():
            heapq.heappush(heap, (-value,key))
        
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans