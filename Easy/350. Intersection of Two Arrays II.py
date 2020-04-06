from collections import Counter
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        return list((count1&count2).elements())