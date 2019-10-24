class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        for index,num1 in enumerate(numbers):
            right = len(numbers) -1
            mid = right
            left = index+1
            newTarget = target - num1
            
            while left <= right:
                mid = (left+right) // 2
                midVal = numbers[mid]
                if midVal < newTarget:
                    left = mid + 1
                elif midVal > newTarget:
                    right = mid - 1
                else:
                    return [index+1,mid+1]