class Solution:
    def maxArea(self, height: list) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            curArea = min(height[left],height[right]) * (right - left)
            area = max(curArea,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area