class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = 0
        k = 0
        while nums2 and index < m + k:
            if nums2[0] <= nums1[index]:
                nums1.insert(index,nums2.pop(0))
                k += 1
            else:
                index += 1
        
        while nums2:
            nums1[index] = nums2.pop(0)
            index += 1
            
        while k:
            nums1.pop()
            k -= 1