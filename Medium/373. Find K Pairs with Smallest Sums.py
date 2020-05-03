import heapq
class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        if not nums1 or not nums2:
            return None
        
        k = min(k, len(nums1)*len(nums2))
        
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1+num2, num1,num2))
                
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1:])
            
        return ans