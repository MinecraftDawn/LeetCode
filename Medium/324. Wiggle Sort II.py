class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)
        mid = length//2+1 if length % 2 else length //2
        tmp1 = nums[:mid][::-1]
        tmp2 = nums[mid:][::-1]
        
        for i in range(length):
            if i % 2 == 0:
                nums[i] = tmp1.pop(0)
            else:
                nums[i] = tmp2.pop(0)
                
        return nums