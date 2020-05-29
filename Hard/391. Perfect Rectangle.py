class Solution:
    def isRectangleCover(self, rectangles: list) -> bool:
        rectRange = [[float("inf"), float("inf")], [float("-inf"), float("-inf")]]
        sumArea = 0
        for rect in rectangles:
            rectRange[0] = min(rectRange[0], rect[:2])
            rectRange[1] = max(rectRange[1], rect[2:])

            sumArea += (rect[2] - rect[0]) * (rect[3] - rect[1])

        return (rectRange[1][0] - rectRange[0][0]) * (rectRange[1][1] - rectRange[0][1]) == sumArea
