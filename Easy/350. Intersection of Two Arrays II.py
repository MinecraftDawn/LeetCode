from collections import Counter
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        count1 = Counter(nums1)
        ans = []
        
        for num in nums2:
            if count1.get(num):
                count1[num] -= 1
                ans.append(num)
                
        return ans