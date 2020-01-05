import bisect
class Solution:
    def searchMatrix(self, matrix:list, target:int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(len(matrix)):
            index = bisect.bisect_left(matrix[i], target)
            if index < len(matrix[i]) and matrix[i][index] == target:
                return True
        return False