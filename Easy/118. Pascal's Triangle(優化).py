class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows: return []
        ans = [[1]]
        
        for i in range(1, numRows):
            preArr = ans[-1]
            curArr = [1]
            for j in range(len(preArr)-1):
                curArr.append(preArr[j]+preArr[j+1])
            curArr.append(1)
            ans.append(curArr)
        
        return ans