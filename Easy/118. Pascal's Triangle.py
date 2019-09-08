class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows: return []
        ans = [[1],[1,1]]
        
        
        for i in range(3, numRows+1):
            if i % 2 == 0:
                preArr = ans[-1][:i//2+1]
                curArr = [1]
                for j in range(len(preArr)-2):
                    curArr.append(preArr[j]+preArr[j+1])
                curArr += curArr[::-1]
                ans.append(curArr)
            else:
                preArr = ans[-1][:i//2]
                curArr = [1]
                for j in range(len(preArr)-1):
                    curArr.append(preArr[j]+preArr[j+1])
                curArr += [preArr[-1]*2] + curArr[::-1]
                ans.append(curArr)
        
        return ans[:numRows]