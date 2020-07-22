# Reference: https://www.cnblogs.com/grandyang/p/5933787.html

class Solution:
    def splitArray(self, nums: list, m: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            count, cur = 1, 0

            for num in nums:
                cur += num
                if cur > mid:
                    cur = num
                    count += 1

            if count <= m:
                right = mid
            else:
                left = mid + 1

        return left