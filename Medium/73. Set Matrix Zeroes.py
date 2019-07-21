class Solution:
    def setZeroes(self, matrix: list) -> None:
        colList = [1] * len(matrix)
        rowList = [1] * len(matrix[0])
        
        for rowNum,row in enumerate(matrix):
            for colNum,element in enumerate(row):
                if not element:
                    # col
                    if rowList[colNum]:
                        rowList[colNum] = 0
                            
                    # row
                    if colList[rowNum]:
                        colList[rowNum] = 0
                        
        for c,i in enumerate(colList):
            if not i:
                for j in range(len(matrix[0])):
                    matrix[c][j] = 0
                    
        for c,i in enumerate(rowList):
            if not i:
                for j in range(len(matrix)):
                    matrix[j][c] = 0