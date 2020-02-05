class NumArray:
    def __init__(self, nums: list):
        self.dp = [0]
        tmp = 0
        for num in nums:
            tmp += num
            self.dp.append(tmp)
        print(self.dp)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)