class Solution:
    def spiralOrder(self, matrix: list) -> list:
        ans = []
        while len(matrix) > 0:
            ans += matrix.pop(0)
            
            if len(matrix) > 0:
                for i in matrix:
                    ans += [i.pop()]
                if not i:
                    return ans                        
            
            if len(matrix) > 0:
                tmp = matrix.pop()
                tmp.reverse()
                ans += tmp
            
            if len(matrix) > 0:
                for i in range(len(matrix)-1,-1,-1):
                    ans += [matrix[i].pop(0)]
                if len(matrix[0]) == 0:
                    return ans
                
        return ans