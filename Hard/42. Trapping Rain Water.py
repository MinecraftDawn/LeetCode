class Solution:
    def trap(self, height: list) -> int:
        if not height: return 0
        leftList = []
        rightList = []
        leftH = height[0]
        rightH = height[len(height)-1]
        sumWater = 0
        
        for c,h in enumerate(height):
            if h > leftH:
                leftH = h
            leftList.append(leftH)
            
        for c in range(len(height)-1,-1,-1):
            h = height[c]
            if h > rightH:
                rightH = h
            rightList.insert(0,rightH)
        
        for c,val in enumerate(height):
            sumWater += min(leftList[c],rightList[c]) - val
        
        return sumWater