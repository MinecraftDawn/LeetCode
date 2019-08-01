class Solution:
    def largestRectangleArea(self, heights:list) -> int:
        ans = 0
        stack = []
        
        index = 0
        while index < len(heights):
            val = heights[index]
            if not stack or heights[stack[-1]] < val:
                stack.append(index)
                index += 1
            else:
                pop = stack.pop()
                if stack:
                    area = heights[pop] * (index - stack[-1] - 1)
                else:
                    area = heights[pop] * index
                ans = max(area,ans)
                
        while stack:
            pop = stack.pop()
            if stack:
                    area = heights[pop] * (index - stack[-1] - 1)
            else:
                area = heights[pop] * index
            ans = max(area,ans)
        return ans