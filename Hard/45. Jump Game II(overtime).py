class Solution:
    def jump(self, nums: list) -> int:
        if not nums: return 0
        self.nums = nums
        self.len = len(nums)
        self.breadth = []
        self.dp = [1048576] * len(nums)
        
        self.dfs(0,1)
        
        return self.dp.pop() - 1
        
    def dfs(self,index,step):
        if index >= self.len: return
        if self.dp[index] > step:
            self.dp[index] = step
            
            num = self.nums[index]
            for i in range(1,num+1):
                self.breadth.append([index+i,step+1])
                
            while self.breadth:
                get = self.breadth.pop(0)
                self.dfs(get[0],get[1])
        else:
            return