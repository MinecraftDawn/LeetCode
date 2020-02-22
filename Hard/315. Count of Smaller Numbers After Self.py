import bisect
class Solution:
    def countSmaller(self, nums: list) -> list:
        ans = []
        pos = []
        for i,num in enumerate(nums[::-1]):
            index = bisect.bisect_left(pos, num)
            ans.append(index)
            bisect.insort_left(pos, num)
            
        return ans[::-1]