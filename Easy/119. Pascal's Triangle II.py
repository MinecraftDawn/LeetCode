class Solution:
    def getRow(self, rowIndex: int) -> list:
        ans = [[1]]
        
        for i in range(1, rowIndex+1):
            preArr = ans[-1]
            curArr = [1]
            for j in range(len(preArr)-1):
                curArr.append(preArr[j]+preArr[j+1])
            curArr.append(1)
            ans.append(curArr)
        
        return ans[-1]