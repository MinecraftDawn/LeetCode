class Solution:
    def maxSubArray(self, nums: list) -> int:
        return self.findMaxSubarray(nums,0,len(nums)-1)
                
    def findMaxCenterSubarray(self,array,low,mid,high):
        lSum = array[mid]
        rSum = array[mid+1]
        
        runSum = 0
        for i in range(mid,low-1,-1):
            runSum += array[i]
            lSum = max(runSum,lSum)
            
        runSum = 0
        for i in range(mid+1,high+1):
            runSum += array[i]
            rSum = max(runSum,rSum)
            
        return lSum + rSum
    
    def findMaxSubarray(self,array,low,high):
        if low == high: 
            return array[low]
        
        mid = (low + high) // 2
        
        lSum = self.findMaxSubarray(array,low,mid)
        rSum = self.findMaxSubarray(array,mid+1,high)
        mSum = self.findMaxCenterSubarray(array,low,mid,high)
        
        return max(lSum,rSum,mSum)