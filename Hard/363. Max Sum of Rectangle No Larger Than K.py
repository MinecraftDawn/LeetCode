# Reference: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/233938/Python-code-with-comments-explaining-the-algorithm
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: list, k: int) -> int:
        if not matrix or not matrix[0]: return 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        if row > col:
            matrix = list(zip(*matrix))
            row,col = col,row
        
        ans = float("-inf")
        
        for start in range(row):
            sums = [0] * col
            for end in range(start, row):
                slist = []
                num = 0
                for y in range(col):
                    sums[y] += matrix[end][y]
                    num += sums[y]
                    if num <= k:
                        ans = max(ans, num)
                    index = bisect.bisect_left(slist, num-k)
                    if index != len(slist):
                        ans = max(ans, num-slist[index])
                    bisect.insort(slist, num)

        return ans