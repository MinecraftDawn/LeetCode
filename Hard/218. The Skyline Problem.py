# reference: https://leetcode.com/problems/the-skyline-problem/discuss/426929/Python3-simple-idea-with-explaination
import heapq
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: list) -> list:    
        lines = []
        heap = []
        heightMap = defaultdict(int)
        points = []
        
        # Notice that left need is False, because tuple sort will use it
        for left, right, height in buildings:
            lines.append((left, height, False))
            lines.append((right, height, True))
        lines.sort()
        
        for line, height, flag in lines:
            if flag == 0:
                heapq.heappush(heap, -height)
                heightMap[height] += 1
            else:
                heightMap[height] -= 1
                while heap and heightMap[-heap[0]] == 0:
                    heapq.heappop(heap)
                  
            if heap:
                maxHeight = -heap[0]
                if not points:
                    points.append([line, maxHeight])
                elif points[-1][1] != maxHeight:
                    if points[-1][0] == line:
                        points[-1][1] = max(maxHeight, points[-1][1])
                    else:
                        points.append([line, maxHeight])
            else:
                points.append([line, 0])
                
        return points