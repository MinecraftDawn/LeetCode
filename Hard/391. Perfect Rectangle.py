class Solution:
    def isRectangleCover(self, rectangles: list) -> bool:
        sumArea = 0

        angleSet = set()
        for rect in rectangles:
            angles = [(rect[0], rect[1]),
                      (rect[0], rect[3]),
                      (rect[2], rect[1]),
                      (rect[2], rect[3])]

            for angle in angles:
                if angle in angleSet:
                    angleSet.remove(angle)
                else:
                    angleSet.add(angle)

            sumArea += (rect[2] - rect[0]) * (rect[3] - rect[1])

        if len(angleSet) != 4: return False
        angleSet = sorted(list(angleSet))

        return (angleSet[3][1] - angleSet[0][1]) * (angleSet[3][0] - angleSet[0][0]) == sumArea