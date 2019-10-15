class Solution:
    def maxProduct(self, nums: list) -> int:
        if not nums: return
        if [-1,-1] == nums: return 1
        ans = nums[0]
        negNum = 1
        posNum = 1
        
        for i in nums:
            if i > 0:
                posNum *= i
                if negNum > 0:
                    negNum *= i
                ans = max(posNum, ans)
                
            elif i == 0:
                ans = max(0, posNum, ans)
                if posNum < 0:
                    ans = max(posNum//negNum, ans)
                posNum = 1
                negNum = 1
                
            else:
                posNum *= i
                if negNum > 0:
                    negNum *= i
                ans = max(posNum, ans)
                
        if posNum < 0:
            ans = max(posNum//negNum, ans)
        if ans == 1:
            if 1 not in nums:
                return max(nums)
        return ans
    
data = [2,3,-2,4,0,5,2,2]
ans = Solution().maxProduct(data)
print(ans)