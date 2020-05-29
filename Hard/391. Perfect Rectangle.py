class Solution:
    def isRectangleCover(self, rectangles: list) -> bool:
        rectRange = [[float("inf"), float("inf")],
                     [float("inf"),float("-inf")],
                     [float("-inf"), float("inf")],
                     [float("-inf"), float("-inf")]]
        sumArea = 0
        for rect in rectangles:
            rectRange[0] = min(rectRange[0], rect[:2])
            if rect[0] <= rectRange[1][0] and rect[3] >= rectRange[1][1]:
                rectRange[1] = [rect[0], rect[3]]
            if rect[2] >= rectRange[2][0] and rect[1] <= rectRange[2][1]:
                rectRange[2] = [rect[2], rect[1]]
            rectRange[3] = max(rectRange[3], rect[2:])

            sumArea += (rect[2] - rect[0]) * (rect[3] - rect[1])

        return (rectRange[3][0] - rectRange[0][0]) * (rectRange[3][1] - rectRange[0][1]) == (rectRange[2][0] - rectRange[1][0]) * (rectRange[1][1] - rectRange[2][1]) == sumArea
