class Solution:
    def maxPoints(self, points: list) -> int:
        length = len(points)
        if length < 3: return length
        
        ans = 0
        for i in range(length-1):
            for j in range(i+1,length):
                x1,y1 = points[i]
                x2,y2 = points[j]
                
                dx = x2-x1
                dy = y2-y1
                
                count = 0
                for k in range(length):
                    x3,y3 = points[k]
                    if dx == 0:
                        if x3 == x1:
                            count += 1
                    else:
                        if dy*(x3-x1) == dx*(y3-y1):
                            count += 1
                            
                ans = max(ans,count)
        return ans