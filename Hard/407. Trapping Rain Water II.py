# Reference: https://leetcode.com/problems/trapping-rain-water-ii/discuss/602401/Python-heapq-solution-with-nice-explaination-easy-to-understand!!!
import heapq


class Solution:
    def trapRainWater(self, heightMap: list) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2: return 0

        heap = []
        visted = set()

        for row in (0, len(heightMap) - 1):
            for col in range(len(heightMap[0])):
                heapq.heappush(heap, (heightMap[row][col], row, col))
                visted.add((row, col))
        for row in range(len(heightMap)):
            for col in (0, len(heightMap[0]) - 1):
                heapq.heappush(heap, (heightMap[row][col], row, col))
                visted.add((row, col))

        ans = 0

        while heap:
            height, row, col = heapq.heappop(heap)

            for dRow, dCol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxtRow = row + dRow
                nxtCol = col + dCol

                if (nxtRow, nxtCol) not in visted and 0 <= nxtRow < len(heightMap) and 0 <= nxtCol < len(heightMap[0]):
                    nxtHeight = heightMap[nxtRow][nxtCol]
                    ans += max(0, height - nxtHeight)
                    heapq.heappush(heap, (max(height, nxtHeight), nxtRow, nxtCol))
                    visted.add((nxtRow, nxtCol))
        return ans