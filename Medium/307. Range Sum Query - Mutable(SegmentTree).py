class SegmentTree:
    def __init__(self, num: list):
        self.n = len(num)
        self.tree = [0] * (self.n * 2)
        
        for i in range(self.n):
            self.tree[self.n+i] = num[i]
            
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
    
    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        
        run = index
        while run > 1:
            self.tree[run//2] = self.tree[run] + self.tree[run^1]
            run //= 2
            
    def quary(self, left, right):
        ans = 0
        left += self.n
        right += self.n + 1
        
        while left < right:
            if left & 1:
                ans += self.tree[left]
                left += 1
                
            if right & 1:
                right -= 1
                ans += self.tree[right]
                
            left //= 2
            right //= 2
            
        return ans

class NumArray:

    def __init__(self, nums: list):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        
        for i in range(self.n):
            self.tree[self.n+i] = nums[i]
            
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, i: int, val: int) -> None:
        i+= self.n
        self.tree[i] = val
        
        run = i
        while run > 1:
            self.tree[run//2] = self.tree[run] + self.tree[run^1]
            run //= 2
        
    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        left += self.n
        right += self.n + 1
        
        while left < right:
            if left & 1:
                ans += self.tree[left]
                left += 1
                
            if right & 1:
                right -= 1
                ans += self.tree[right]
                
            left //= 2
            right //= 2
            
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)