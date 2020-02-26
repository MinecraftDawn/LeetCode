class Solution:
    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:
        ans = []
        len1 = len(nums1)
        len2 = len(nums2)
        
        for index1 in range(k+1):
            index2 = k - index1
            if index1 > len1 or index2 > len2: continue
        
            left = self.fineMax(nums1, index1)
            right = self.fineMax(nums2, index2)
            cur = self.merge(left, right)
            ans = max(ans, cur)
        
        return ans
            
        
    def fineMax(self, nums, end):
        size = len(nums)
        maxList = [float('-inf')] * end
        
        j = 0
        for i in range(size):
            while end+i-j < size and j > 0 and maxList[j-1] < nums[i]:
                j -= 1
            if j < end:
                maxList[j] = nums[i]
                j += 1
        return maxList
    
    def merge(self, nums1, nums2):
        merList = []
        while nums1 and nums2:
            if nums1 > nums2:
                merList.append(nums1.pop(0))
            else:
                merList.append(nums2.pop(0))
                
        while nums1: merList.append(nums1.pop(0))
        while nums2: merList.append(nums2.pop(0))
        
        return merList