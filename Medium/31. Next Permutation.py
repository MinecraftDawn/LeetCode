class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        increaseNum = 0
        
        i = 0
        for i in range(numsLen-1,-1,-1):
            if nums[i] >= increaseNum:
                increaseNum = nums[i]
            else:
                break
        
        biggerNum = (9999999,9999999)
        for j in range(numsLen-1,i,-1):
            if nums[j] > nums[i]:
                if nums[j] < biggerNum[0]:
                    biggerNum = (nums[j],j)
                    
        if biggerNum == (9999999,9999999): 
            nums.sort()
            return
        
        nums[i],nums[biggerNum[1]] = nums[biggerNum[1]],nums[i]
        
        startTrans = i+1
        for j in range(startTrans,startTrans+(numsLen-startTrans)//2):
            nums[j],nums[numsLen-1-j+startTrans] = nums[numsLen-1-j+startTrans],nums[j]
        