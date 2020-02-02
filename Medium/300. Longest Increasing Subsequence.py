import bisect
class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        dp = []
        
        for num in nums:
            smallFlag = True
            for tmpList in dp:
                if tmpList[-1] < num:
                    tmpList.append(num)
                    smallFlag = False
            if smallFlag:
                dp.append([num])
                
        for i in range(len(dp)-1,0,-1):
            start = dp[i][0]

            for j in range(i-1,-1,-1):
                index = bisect.bisect_left(dp[j], start)
                if index == 0: continue
                if index + len(dp[i]) > len(dp[j]):
                    dp[j] = dp[j][:index] + dp[i]

        return max([len(tmpList) for tmpList in dp] + [0])