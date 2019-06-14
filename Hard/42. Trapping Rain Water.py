class Solution:
    def trap(self, height: list) -> int:
        if not height: return 0
        rightList = []
        leftH = height[0]
        rightH = height[len(height)-1]
        sumWater = 0
        
        for c in range(len(height)-1,-1,-1):
            h = height[c]
            if h > rightH:
                rightH = h
            rightList.insert(0,rightH)
        
        for c,h in enumerate(height):
            if h > leftH:
                leftH = h
            sumWater += min(leftH,rightList[c]) - h
        
        return sumWater