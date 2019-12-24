class Solution:
    def summaryRanges(self, nums: list) -> list:
        if not nums: return []
        
        ans = []
        tmpList = []
        start = 0
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                tmpList.append([start,i])
                start = i+1
        tmpList.append([start,len(nums)-1])
        
        for start,end in tmpList:
            if start == end:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[end]))
        
        return ans