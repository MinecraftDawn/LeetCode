class Solution:
    def maximalRectangle(self, matrix: list) -> int:
        if not matrix: return 0
        
        rowSize = len(matrix[0])
        left = [0]*rowSize
        right = [rowSize]*rowSize
        height = [0]*rowSize
        ans = 0
        
        for row in matrix:
            curRight = rowSize
            for i in range(rowSize-1, -1, -1):
                if row[i] == '1':
                    right[i] = min(right[i], curRight)
                else:
                    right[i] = rowSize
                    curRight = i
            
            curLeft = 0
            for i in range(rowSize):
                if row[i] == '1':
                    left[i] = max(left[i], curLeft)
                    height[i] = height[i] + 1
                    ans = max(ans,height[i]*(right[i]-left[i]))
                else:
                    left[i] = 0
                    height[i] = 0
                    curLeft = i + 1
                ans = max(ans,height[i]*(right[i]-left[i]))
                
        return ans